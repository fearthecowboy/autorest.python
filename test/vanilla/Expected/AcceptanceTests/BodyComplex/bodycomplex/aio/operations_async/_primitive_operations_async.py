# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.pipeline import ClientRawResponse

from ... import models


class PrimitiveOperations:
    """PrimitiveOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    async def get_int(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get complex types with integer properties.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: IntWrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.IntWrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_int.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('IntWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_int.metadata = {'url': '/complex/primitive/integer'}

    async def put_int(
            self, complex_body, *, custom_headers=None, raw=False, **operation_config):
        """Put complex types with integer properties.

        :param complex_body: Please put -1 and 2
        :type complex_body: ~bodycomplex.models.IntWrapper
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_int.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'IntWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_int.metadata = {'url': '/complex/primitive/integer'}

    async def get_long(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get complex types with long properties.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LongWrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.LongWrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_long.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('LongWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_long.metadata = {'url': '/complex/primitive/long'}

    async def put_long(
            self, complex_body, *, custom_headers=None, raw=False, **operation_config):
        """Put complex types with long properties.

        :param complex_body: Please put 1099511627775 and -999511627788
        :type complex_body: ~bodycomplex.models.LongWrapper
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_long.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'LongWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_long.metadata = {'url': '/complex/primitive/long'}

    async def get_float(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get complex types with float properties.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: FloatWrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.FloatWrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_float.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('FloatWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_float.metadata = {'url': '/complex/primitive/float'}

    async def put_float(
            self, complex_body, *, custom_headers=None, raw=False, **operation_config):
        """Put complex types with float properties.

        :param complex_body: Please put 1.05 and -0.003
        :type complex_body: ~bodycomplex.models.FloatWrapper
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_float.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'FloatWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_float.metadata = {'url': '/complex/primitive/float'}

    async def get_double(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get complex types with double properties.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DoubleWrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.DoubleWrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_double.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DoubleWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_double.metadata = {'url': '/complex/primitive/double'}

    async def put_double(
            self, complex_body, *, custom_headers=None, raw=False, **operation_config):
        """Put complex types with double properties.

        :param complex_body: Please put 3e-100 and
         -0.000000000000000000000000000000000000000000000000000000005
        :type complex_body: ~bodycomplex.models.DoubleWrapper
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_double.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'DoubleWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_double.metadata = {'url': '/complex/primitive/double'}

    async def get_bool(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get complex types with bool properties.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: BooleanWrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.BooleanWrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_bool.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('BooleanWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_bool.metadata = {'url': '/complex/primitive/bool'}

    async def put_bool(
            self, complex_body, *, custom_headers=None, raw=False, **operation_config):
        """Put complex types with bool properties.

        :param complex_body: Please put true and false
        :type complex_body: ~bodycomplex.models.BooleanWrapper
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_bool.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'BooleanWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_bool.metadata = {'url': '/complex/primitive/bool'}

    async def get_string(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get complex types with string properties.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: StringWrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.StringWrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_string.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('StringWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_string.metadata = {'url': '/complex/primitive/string'}

    async def put_string(
            self, complex_body, *, custom_headers=None, raw=False, **operation_config):
        """Put complex types with string properties.

        :param complex_body: Please put 'goodrequest', '', and null
        :type complex_body: ~bodycomplex.models.StringWrapper
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_string.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'StringWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_string.metadata = {'url': '/complex/primitive/string'}

    async def get_date(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get complex types with date properties.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DateWrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.DateWrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DateWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_date.metadata = {'url': '/complex/primitive/date'}

    async def put_date(
            self, complex_body, *, custom_headers=None, raw=False, **operation_config):
        """Put complex types with date properties.

        :param complex_body: Please put '0001-01-01' and '2016-02-29'
        :type complex_body: ~bodycomplex.models.DateWrapper
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'DateWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_date.metadata = {'url': '/complex/primitive/date'}

    async def get_date_time(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get complex types with datetime properties.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DatetimeWrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.DatetimeWrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DatetimeWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_date_time.metadata = {'url': '/complex/primitive/datetime'}

    async def put_date_time(
            self, complex_body, *, custom_headers=None, raw=False, **operation_config):
        """Put complex types with datetime properties.

        :param complex_body: Please put '0001-01-01T12:00:00-04:00' and
         '2015-05-18T11:38:00-08:00'
        :type complex_body: ~bodycomplex.models.DatetimeWrapper
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'DatetimeWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_date_time.metadata = {'url': '/complex/primitive/datetime'}

    async def get_date_time_rfc1123(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get complex types with datetimeRfc1123 properties.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Datetimerfc1123Wrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.Datetimerfc1123Wrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_date_time_rfc1123.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Datetimerfc1123Wrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_date_time_rfc1123.metadata = {'url': '/complex/primitive/datetimerfc1123'}

    async def put_date_time_rfc1123(
            self, complex_body, *, custom_headers=None, raw=False, **operation_config):
        """Put complex types with datetimeRfc1123 properties.

        :param complex_body: Please put 'Mon, 01 Jan 0001 12:00:00 GMT' and
         'Mon, 18 May 2015 11:38:00 GMT'
        :type complex_body: ~bodycomplex.models.Datetimerfc1123Wrapper
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_date_time_rfc1123.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'Datetimerfc1123Wrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_date_time_rfc1123.metadata = {'url': '/complex/primitive/datetimerfc1123'}

    async def get_duration(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get complex types with duration properties.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DurationWrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.DurationWrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_duration.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DurationWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_duration.metadata = {'url': '/complex/primitive/duration'}

    async def put_duration(
            self, field=None, *, custom_headers=None, raw=False, **operation_config):
        """Put complex types with duration properties.

        :param field:
        :type field: timedelta
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        complex_body = models.DurationWrapper(field=field)

        # Construct URL
        url = self.put_duration.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'DurationWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_duration.metadata = {'url': '/complex/primitive/duration'}

    async def get_byte(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get complex types with byte properties.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ByteWrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.ByteWrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_byte.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ByteWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_byte.metadata = {'url': '/complex/primitive/byte'}

    async def put_byte(
            self, field=None, *, custom_headers=None, raw=False, **operation_config):
        """Put complex types with byte properties.

        :param field:
        :type field: bytearray
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        complex_body = models.ByteWrapper(field=field)

        # Construct URL
        url = self.put_byte.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'ByteWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_byte.metadata = {'url': '/complex/primitive/byte'}
