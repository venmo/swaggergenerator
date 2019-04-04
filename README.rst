swaggergenerator
=================

*[not actively supported outside of internal Venmo usage]*

Creating swagger/OAS specs for an existing api by hand is tedious and error-prone.
swaggergenerator fixes this by creating schemas from example interactions:

Generation is a three step process.
Here's an example using `httpbin <https://httpbin.org/get>`__:

.. code-block:: python

    import requests
    from swaggergenerator import Generator, get_yaml

    # 1: Create a Generator.
    generator = Generator()

    # 2: Provide one or more examples. They can be for different paths and verbs.
    response = requests.get('https://httpbin.org/get')
    generator.provide_example(response.request, response)

    # 3: Generate a schema (specifically, a Swagger Paths Object).
    print get_yaml(generator.generate_paths())

.. code-block:: yaml

  /get:
    get:
      description: TODO
      parameters: []
      responses:
        '200':
          description: TODO
          schema:
            additionalProperties: false
            properties:
              args:
                additionalProperties: false
                properties: {}
                type: object
              headers:
                additionalProperties: false
                properties:
                  Accept:
                    type: string
                  Accept-Encoding:
                    type: string
                  Connection:
                    type: string
                  Content-Length:
                    type: string
                  Host:
                    type: string
                  User-Agent:
                    type: string
                type: object
              origin:
                type: string
              url:
                type: string
            type: object

You can install it with ``$ pip install swaggergenerator``.


Generation details
---------------------

Generally, the generated schemas err on the side of being too strict.
For example, additionalProperties is always set to False and parameters are always required.
The recommended workflow is to generate schemas, validate them against all interactions in your test suite, and iterate until tests pass.

Here are the swagger features you can expect to be generated:

- path objects for arbitrary verb/path combinations
- all-digit path parameters
- complex path parameters (when given alongside an all-digit example)
- request schemas for 2xx responses
- response schemas for 2xx responses
- references to existing definitions

Here are some swagger features that won't be generated.
If your api uses any of these, you'll need to fix up your output manually:

- nullable/polymorphic types
- heterogeneous arrays
- optional properties
- additionalProperties != False


Contributing
------------

Inside your vitualenv:

.. code-block:: bash

    $ cd swaggergenerator
    $ pip install -e .
    $ pip install -r requirements.txt


To run the tests:

.. code-block:: bash

    $ py.test tests/
