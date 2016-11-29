# coding: utf-8

"""
    BitMEX API

    REST API for the BitMEX.com trading platform.<br><br><a href=\"/app/restAPI\">REST Documentation</a><br><a href=\"/app/wsAPI\">Websocket Documentation</a>

    OpenAPI spec version: 1.2.0
    Contact: support@bitmex.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Transaction(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, transact_id=None, account=None, currency=None, transact_type=None, amount=None, fee=None, transact_status=None, address=None, tx=None, text=None, transact_time=None, timestamp=None):
        """
        Transaction - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'transact_id': 'str',
            'account': 'float',
            'currency': 'str',
            'transact_type': 'str',
            'amount': 'float',
            'fee': 'float',
            'transact_status': 'str',
            'address': 'str',
            'tx': 'str',
            'text': 'str',
            'transact_time': 'date',
            'timestamp': 'date'
        }

        self.attribute_map = {
            'transact_id': 'transactID',
            'account': 'account',
            'currency': 'currency',
            'transact_type': 'transactType',
            'amount': 'amount',
            'fee': 'fee',
            'transact_status': 'transactStatus',
            'address': 'address',
            'tx': 'tx',
            'text': 'text',
            'transact_time': 'transactTime',
            'timestamp': 'timestamp'
        }

        self._transact_id = transact_id
        self._account = account
        self._currency = currency
        self._transact_type = transact_type
        self._amount = amount
        self._fee = fee
        self._transact_status = transact_status
        self._address = address
        self._tx = tx
        self._text = text
        self._transact_time = transact_time
        self._timestamp = timestamp

    @property
    def transact_id(self):
        """
        Gets the transact_id of this Transaction.


        :return: The transact_id of this Transaction.
        :rtype: str
        """
        return self._transact_id

    @transact_id.setter
    def transact_id(self, transact_id):
        """
        Sets the transact_id of this Transaction.


        :param transact_id: The transact_id of this Transaction.
        :type: str
        """

        self._transact_id = transact_id

    @property
    def account(self):
        """
        Gets the account of this Transaction.


        :return: The account of this Transaction.
        :rtype: float
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this Transaction.


        :param account: The account of this Transaction.
        :type: float
        """

        self._account = account

    @property
    def currency(self):
        """
        Gets the currency of this Transaction.


        :return: The currency of this Transaction.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Transaction.


        :param currency: The currency of this Transaction.
        :type: str
        """

        self._currency = currency

    @property
    def transact_type(self):
        """
        Gets the transact_type of this Transaction.


        :return: The transact_type of this Transaction.
        :rtype: str
        """
        return self._transact_type

    @transact_type.setter
    def transact_type(self, transact_type):
        """
        Sets the transact_type of this Transaction.


        :param transact_type: The transact_type of this Transaction.
        :type: str
        """

        self._transact_type = transact_type

    @property
    def amount(self):
        """
        Gets the amount of this Transaction.


        :return: The amount of this Transaction.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Transaction.


        :param amount: The amount of this Transaction.
        :type: float
        """

        self._amount = amount

    @property
    def fee(self):
        """
        Gets the fee of this Transaction.


        :return: The fee of this Transaction.
        :rtype: float
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """
        Sets the fee of this Transaction.


        :param fee: The fee of this Transaction.
        :type: float
        """

        self._fee = fee

    @property
    def transact_status(self):
        """
        Gets the transact_status of this Transaction.


        :return: The transact_status of this Transaction.
        :rtype: str
        """
        return self._transact_status

    @transact_status.setter
    def transact_status(self, transact_status):
        """
        Sets the transact_status of this Transaction.


        :param transact_status: The transact_status of this Transaction.
        :type: str
        """

        self._transact_status = transact_status

    @property
    def address(self):
        """
        Gets the address of this Transaction.


        :return: The address of this Transaction.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Transaction.


        :param address: The address of this Transaction.
        :type: str
        """

        self._address = address

    @property
    def tx(self):
        """
        Gets the tx of this Transaction.


        :return: The tx of this Transaction.
        :rtype: str
        """
        return self._tx

    @tx.setter
    def tx(self, tx):
        """
        Sets the tx of this Transaction.


        :param tx: The tx of this Transaction.
        :type: str
        """

        self._tx = tx

    @property
    def text(self):
        """
        Gets the text of this Transaction.


        :return: The text of this Transaction.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Transaction.


        :param text: The text of this Transaction.
        :type: str
        """

        self._text = text

    @property
    def transact_time(self):
        """
        Gets the transact_time of this Transaction.


        :return: The transact_time of this Transaction.
        :rtype: date
        """
        return self._transact_time

    @transact_time.setter
    def transact_time(self, transact_time):
        """
        Sets the transact_time of this Transaction.


        :param transact_time: The transact_time of this Transaction.
        :type: date
        """

        self._transact_time = transact_time

    @property
    def timestamp(self):
        """
        Gets the timestamp of this Transaction.


        :return: The timestamp of this Transaction.
        :rtype: date
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this Transaction.


        :param timestamp: The timestamp of this Transaction.
        :type: date
        """

        self._timestamp = timestamp

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other