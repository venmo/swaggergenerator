import requests

from swaggergenerator import Generator, get_yaml


def test_no_params(httpbin):
    generator = Generator()
    response = requests.get(httpbin.url + '/get')
    generator.provide_example(response.request, response)

    response = requests.post(httpbin.url + '/post')
    generator.provide_example(response.request, response)

    expected = {u'/post': {'post': {'responses': {'200': {'description': 'TODO', 'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'files': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'origin': {'type': 'string'}, u'form': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'url': {'type': 'string'}, u'args': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'headers': {'additionalProperties': False, 'type': 'object', 'properties': {u'Content-Length': {'type': 'string'}, u'Accept-Encoding': {'type': 'string'}, u'Connection': {'type': 'string'}, u'Accept': {'type': 'string'}, u'User-Agent': {'type': 'string'}, u'Host': {'type': 'string'}}}, u'json': {'type': 'null'}, u'data': {'type': 'string'}}}}}, 'parameters': [], 'description': 'TODO'}}, u'/get': {'get': {'responses': {'200': {'description': 'TODO', 'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'origin': {'type': 'string'}, u'headers': {'additionalProperties': False, 'type': 'object', 'properties': {u'Content-Length': {'type': 'string'}, u'Accept-Encoding': {'type': 'string'}, u'Connection': {'type': 'string'}, u'Accept': {'type': 'string'}, u'User-Agent': {'type': 'string'}, u'Host': {'type': 'string'}}}, u'args': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'url': {'type': 'string'}}}}}, 'parameters': [], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_get_params(httpbin):
    generator = Generator()
    response = requests.get(httpbin.url + '/get', params={'query_key': 'query_val'})
    generator.provide_example(response.request, response)

    expected = {u'/get': {'get': {'responses': {'200': {'description': 'TODO', 'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'origin': {'type': 'string'}, u'headers': {'additionalProperties': False, 'type': 'object', 'properties': {u'Content-Length': {'type': 'string'}, u'Accept-Encoding': {'type': 'string'}, u'Connection': {'type': 'string'}, u'Accept': {'type': 'string'}, u'User-Agent': {'type': 'string'}, u'Host': {'type': 'string'}}}, u'args': {'additionalProperties': False, 'type': 'object', 'properties': {u'query_key': {'type': 'string'}}}, u'url': {'type': 'string'}}}}}, 'parameters': [{'required': True, 'type': 'string', 'name': 'query_key', 'in': 'query'}], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_post_body(httpbin):
    generator = Generator()
    response = requests.post(httpbin.url + '/post', json={'body_key': {'body_subkey': 'body_val'}})
    generator.provide_example(response.request, response)

    expected = {u'/post': {'post': {'responses': {'200': {'description': 'TODO', 'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'files': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'origin': {'type': 'string'}, u'form': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'url': {'type': 'string'}, u'args': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'headers': {'additionalProperties': False, 'type': 'object', 'properties': {u'Content-Length': {'type': 'string'}, u'Accept-Encoding': {'type': 'string'}, u'Connection': {'type': 'string'}, u'Accept': {'type': 'string'}, u'User-Agent': {'type': 'string'}, u'Host': {'type': 'string'}, u'Content-Type': {'type': 'string'}}}, u'json': {'additionalProperties': False, 'type': 'object', 'properties': {u'body_key': {'additionalProperties': False, 'type': 'object', 'properties': {u'body_subkey': {'type': 'string'}}}}}, u'data': {'type': 'string'}}}}}, 'parameters': [{'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'body_key': {'additionalProperties': False, 'type': 'object', 'properties': {u'body_subkey': {'type': 'string'}}}}}, 'name': 'body_data', 'in': 'body'}], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_naive_path_params(httpbin):
    generator = Generator()
    response = requests.get(httpbin.url + '/cache/1')
    generator.provide_example(response.request, response)

    response = requests.get(httpbin.url + '/cache/2')
    generator.provide_example(response.request, response)

    expected = {u'/cache/{param1}': {'get': {'responses': {'200': {'description': 'TODO', 'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'origin': {'type': 'string'}, u'headers': {'additionalProperties': False, 'type': 'object', 'properties': {u'Content-Length': {'type': 'string'}, u'Accept-Encoding': {'type': 'string'}, u'Connection': {'type': 'string'}, u'Accept': {'type': 'string'}, u'User-Agent': {'type': 'string'}, u'Host': {'type': 'string'}}}, u'args': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'url': {'type': 'string'}}}}}, 'parameters': [{'required': True, 'type': 'string', 'name': 'param1', 'in': 'path'}], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_component_length_mismatch(httpbin):
    generator = Generator()
    response = requests.get(httpbin.url + '/get')
    generator.provide_example(response.request, response)

    response = requests.get(httpbin.url + '/cache/2')
    generator.provide_example(response.request, response)

    expected = {u'/get': {'get': {'responses': {'200': {'description': 'TODO', 'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'origin': {'type': 'string'}, u'headers': {'additionalProperties': False, 'type': 'object', 'properties': {u'Content-Length': {'type': 'string'}, u'Accept-Encoding': {'type': 'string'}, u'Connection': {'type': 'string'}, u'Accept': {'type': 'string'}, u'User-Agent': {'type': 'string'}, u'Host': {'type': 'string'}}}, u'args': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'url': {'type': 'string'}}}}}, 'parameters': [], 'description': 'TODO'}}, u'/cache/{param1}': {'get': {'responses': {'200': {'description': 'TODO', 'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'origin': {'type': 'string'}, u'headers': {'additionalProperties': False, 'type': 'object', 'properties': {u'Content-Length': {'type': 'string'}, u'Accept-Encoding': {'type': 'string'}, u'Connection': {'type': 'string'}, u'Accept': {'type': 'string'}, u'User-Agent': {'type': 'string'}, u'Host': {'type': 'string'}}}, u'args': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'url': {'type': 'string'}}}}}, 'parameters': [{'required': True, 'type': 'string', 'name': 'param1', 'in': 'path'}], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_non_naive_path_params(httpbin):
    generator = Generator()
    response = requests.get(httpbin.url + '/basic-auth/1/pass', auth=('1', 'pass'))
    generator.provide_example(response.request, response)

    response = requests.get(httpbin.url + '/basic-auth/user/pass', auth=('user', 'pass'))
    generator.provide_example(response.request, response)

    expected = {u'/basic-auth/{param1}/pass': {'get': {'responses': {'200': {'description': 'TODO', 'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'authenticated': {'type': 'boolean'}, u'user': {'type': 'string'}}}}}, 'parameters': [{'required': True, 'type': 'string', 'name': 'param1', 'in': 'path'}], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_custom_path_params(httpbin):
    class CustomGenerator(Generator):
        def is_param(self, e, path):
            return e in {'user1', 'user2'} or super(CustomGenerator, self).is_param(e, path)

    generator = CustomGenerator()
    response = requests.get(httpbin.url + '/basic-auth/user1/pass', auth=('user1', 'pass'))
    generator.provide_example(response.request, response)

    response = requests.get(httpbin.url + '/basic-auth/user2/pass', auth=('user2', 'pass'))
    generator.provide_example(response.request, response)

    expected = {u'/basic-auth/{param1}/pass': {'get': {'responses': {'200': {'description': 'TODO', 'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'authenticated': {'type': 'boolean'}, u'user': {'type': 'string'}}}}}, 'parameters': [{'required': True, 'type': 'string', 'name': 'param1', 'in': 'path'}], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_base_path(httpbin):
    generator = Generator(base_path='/cache')
    response = requests.get(httpbin.url + '/cache/1')
    generator.provide_example(response.request, response)

    response = requests.get(httpbin.url + '/cache/2')
    generator.provide_example(response.request, response)

    expected = {'/{param1}': {'get': {'responses': {'200': {'description': 'TODO', 'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'origin': {'type': 'string'}, u'headers': {'additionalProperties': False, 'type': 'object', 'properties': {u'Content-Length': {'type': 'string'}, u'Accept-Encoding': {'type': 'string'}, u'Connection': {'type': 'string'}, u'Accept': {'type': 'string'}, u'User-Agent': {'type': 'string'}, u'Host': {'type': 'string'}}}, u'args': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'url': {'type': 'string'}}}}}, 'parameters': [{'required': True, 'type': 'string', 'name': 'param1', 'in': 'path'}], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_param_blacklist(httpbin):
    generator = Generator(query_key_blacklist={'token'})
    response = requests.get(httpbin.url + '/get', params={'token': '123'})
    generator.provide_example(response.request, response)

    expected = {u'/get': {'get': {'responses': {'200': {'description': 'TODO', 'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'origin': {'type': 'string'}, u'headers': {'additionalProperties': False, 'type': 'object', 'properties': {u'Content-Length': {'type': 'string'}, u'Accept-Encoding': {'type': 'string'}, u'Connection': {'type': 'string'}, u'Accept': {'type': 'string'}, u'User-Agent': {'type': 'string'}, u'Host': {'type': 'string'}}}, u'args': {'additionalProperties': False, 'type': 'object', 'properties': {u'token': {'type': 'string'}}}, u'url': {'type': 'string'}}}}}, 'parameters': [], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_definition_matching(httpbin):
    existing_schema = {
        'definitions': {
            'Person': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                    },
                    'id': {
                        'type': 'integer',
                    }
                }
            }
        }
    }

    generator = Generator(existing_schema=existing_schema)
    response = requests.post(httpbin.url + '/post', json=[{'name': 'foo', 'id': 1}, {'name': 'bar', 'id': 2}])
    generator.provide_example(response.request, response)

    expected = {u'/post': {'post': {'responses': {'200': {'description': 'TODO', 'schema': {'$ref': '#/definitions/Person'}}}, 'parameters': [{'schema': {'items': {'$ref': '#/definitions/Person'}, 'type': 'array'}, 'name': 'body_data', 'in': 'body'}], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_subdefinition_matching(httpbin):
    existing_schema = {
        'definitions': {
            'Person': {
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'name': {
                        '$ref': '#/definitions/Name',
                    }
                },
            },
            'Name': {
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'first': {
                        type: 'string',
                    },
                    'last': {
                        type: 'string',
                    },
                }
            }
        }
    }

    generator = Generator(existing_schema=existing_schema)
    response = requests.post(httpbin.url + '/post', json={'name': {'first': 'foo', 'last': 'bar'}})
    generator.provide_example(response.request, response)

    expected = {u'/post': {'post': {'responses': {'200': {'description': 'TODO', 'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'files': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'origin': {'type': 'string'}, u'form': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'url': {'type': 'string'}, u'args': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'headers': {'additionalProperties': False, 'type': 'object', 'properties': {u'Content-Length': {'type': 'string'}, u'Accept-Encoding': {'type': 'string'}, u'Connection': {'type': 'string'}, u'Accept': {'type': 'string'}, u'User-Agent': {'type': 'string'}, u'Host': {'type': 'string'}, u'Content-Type': {'type': 'string'}}}, u'json': {'$ref': '#/definitions/Person'}, u'data': {'type': 'string'}}}}}, 'parameters': [{'schema': {'$ref': '#/definitions/Person'}, 'name': 'body_data', 'in': 'body'}], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_empty_array_with_valid_examples(httpbin):
    generator = Generator()
    response = requests.post(httpbin.url + '/post', json=[])
    generator.provide_example(response.request, response)

    response = requests.post(httpbin.url + '/post', json=[1, 2, 3])
    generator.provide_example(response.request, response)

    expected = {u'/post': {'post': {'responses': {'200': {'description': 'TODO', 'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'files': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'origin': {'type': 'string'}, u'form': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'url': {'type': 'string'}, u'args': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'headers': {'additionalProperties': False, 'type': 'object', 'properties': {u'Content-Length': {'type': 'string'}, u'Accept-Encoding': {'type': 'string'}, u'Connection': {'type': 'string'}, u'Accept': {'type': 'string'}, u'User-Agent': {'type': 'string'}, u'Host': {'type': 'string'}, u'Content-Type': {'type': 'string'}}}, u'json': {'items': {'type': 'number'}, 'type': 'array'}, u'data': {'type': 'string'}}}}}, 'parameters': [{'schema': {'items': {'type': 'number'}, 'type': 'array'}, 'name': 'body_data', 'in': 'body'}], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_empty_array_alone_ignored(httpbin):
    generator = Generator()
    response = requests.post(httpbin.url + '/post', json=[])
    generator.provide_example(response.request, response)

    expected = {u'/post': {'post': {'responses': {}, 'parameters': [], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_known_paths_ignored(httpbin):
    existing_schema = {
        'paths': {
            '/get': {
                'get': {}
            }
        }
    }
    generator = Generator(existing_schema=existing_schema)
    response = requests.get(httpbin.url + '/get')
    generator.provide_example(response.request, response)

    expected = {}
    assert generator.generate_paths() == expected


def test_example_str(httpbin):
    generator = Generator()
    response = requests.get(httpbin.url + '/get')
    generator.provide_example(response.request, response)
    assert str(generator.path_to_examples['/get'][0]) == "'get /get -> 200'"


def test_get_yaml(httpbin):
    generator = Generator()
    response = requests.post(httpbin.url + '/post', json=[])
    generator.provide_example(response.request, response)

    expected = {u'/post': {'post': {'responses': {}, 'parameters': [], 'description': 'TODO'}}}
    schemas = generator.generate_paths()
    assert schemas == expected

    expected_yaml = """  /post:
    post:
      description: TODO
      parameters: []
      responses: {}
  """

    assert get_yaml(schemas) == expected_yaml


def test_provided_default(httpbin):
    generator = Generator(default={'description': 'unexpected error', 'schema': {'$ref': '#/definitions/Error'}})
    response = requests.post(httpbin.url + '/get', json=[])
    generator.provide_example(response.request, response)

    expected = {u'/get': {'post': {'responses': {'default': {'description': 'unexpected error', 'schema': {'$ref': '#/definitions/Error'}}}, 'description': 'TODO'}}}
    assert generator.generate_paths() == expected


def test_optional_field_nonempty_example(httpbin):
    generator = Generator()
    response = requests.post(httpbin.url + '/post', json={'parent': {'other': True}})
    generator.provide_example(response.request, response)

    response = requests.post(httpbin.url + '/post', json={'parent': {'optional': True, 'other': True}})
    generator.provide_example(response.request, response)

    expected = {u'/post': {'post': {'responses': {'200': {'description': 'TODO', 'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'files': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'origin': {'type': 'string'}, u'form': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'url': {'type': 'string'}, u'args': {'additionalProperties': False, 'type': 'object', 'properties': {}}, u'headers': {'additionalProperties': False, 'type': 'object', 'properties': {u'Content-Length': {'type': 'string'}, u'Accept-Encoding': {'type': 'string'}, u'Connection': {'type': 'string'}, u'Accept': {'type': 'string'}, u'User-Agent': {'type': 'string'}, u'Host': {'type': 'string'}, u'Content-Type': {'type': 'string'}}}, u'json': {'additionalProperties': False, 'type': 'object', 'properties': {u'parent': {'additionalProperties': False, 'type': 'object', 'properties': {u'other': {'type': 'boolean'}, u'optional': {'type': 'boolean'}}}}}, u'data': {'type': 'string'}}}}}, 'parameters': [{'schema': {'additionalProperties': False, 'type': 'object', 'properties': {u'parent': {'additionalProperties': False, 'type': 'object', 'properties': {u'other': {'type': 'boolean'}, u'optional': {'type': 'boolean'}}}}}, 'name': 'body_data', 'in': 'body'}], 'description': 'TODO'}}}
    assert generator.generate_paths() == expected
