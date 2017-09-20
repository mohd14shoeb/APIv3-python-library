# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  | 

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GetCampaignOverview(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'subject': 'str',
        'type': 'str',
        'status': 'str',
        'scheduled_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'subject': 'subject',
        'type': 'type',
        'status': 'status',
        'scheduled_at': 'scheduledAt'
    }

    def __init__(self, id=None, name=None, subject=None, type=None, status=None, scheduled_at=None):
        """
        GetCampaignOverview - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._subject = None
        self._type = None
        self._status = None
        self._scheduled_at = None

        self.id = id
        self.name = name
        self.subject = subject
        self.type = type
        self.status = status
        if scheduled_at is not None:
          self.scheduled_at = scheduled_at

    @property
    def id(self):
        """
        Gets the id of this GetCampaignOverview.
        ID of the campaign

        :return: The id of this GetCampaignOverview.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GetCampaignOverview.
        ID of the campaign

        :param id: The id of this GetCampaignOverview.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this GetCampaignOverview.
        Name of the campaign

        :return: The name of this GetCampaignOverview.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GetCampaignOverview.
        Name of the campaign

        :param name: The name of this GetCampaignOverview.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def subject(self):
        """
        Gets the subject of this GetCampaignOverview.
        Subject of the campaign

        :return: The subject of this GetCampaignOverview.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this GetCampaignOverview.
        Subject of the campaign

        :param subject: The subject of this GetCampaignOverview.
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")

        self._subject = subject

    @property
    def type(self):
        """
        Gets the type of this GetCampaignOverview.
        Type of campaign

        :return: The type of this GetCampaignOverview.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this GetCampaignOverview.
        Type of campaign

        :param type: The type of this GetCampaignOverview.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["classic", "trigger"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def status(self):
        """
        Gets the status of this GetCampaignOverview.
        Status of the campaign

        :return: The status of this GetCampaignOverview.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this GetCampaignOverview.
        Status of the campaign

        :param status: The status of this GetCampaignOverview.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        allowed_values = ["draft", "sent", "archive", "queued", "suspended", "in_process"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def scheduled_at(self):
        """
        Gets the scheduled_at of this GetCampaignOverview.
        Date on which campaign is scheduled (YYYY-MM-DD HH:mm:ss)

        :return: The scheduled_at of this GetCampaignOverview.
        :rtype: str
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """
        Sets the scheduled_at of this GetCampaignOverview.
        Date on which campaign is scheduled (YYYY-MM-DD HH:mm:ss)

        :param scheduled_at: The scheduled_at of this GetCampaignOverview.
        :type: str
        """
        if scheduled_at is not None and not re.search('^([1-9]\\d{3}-\\d{2}-\\d{2} [0-2]\\d:[0-5]\\d:[0-5]\\d)?$', scheduled_at):
            raise ValueError("Invalid value for `scheduled_at`, must be a follow pattern or equal to `/^([1-9]\\d{3}-\\d{2}-\\d{2} [0-2]\\d:[0-5]\\d:[0-5]\\d)?$/`")

        self._scheduled_at = scheduled_at

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
        if not isinstance(other, GetCampaignOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other