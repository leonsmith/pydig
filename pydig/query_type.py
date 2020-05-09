from enum import Enum

__all__ = ['InvalidQueryType', 'QueryType']


class InvalidQueryType(Exception):

    def __init__(self, query_type):
        self.message = '{} is not a valid query type'.format(repr(query_type))


class QueryType(Enum):
    """
    Enum of all the different record types

    Type IDs are not used in this library but its keeps naming inline with the RFCs:

    Reference: https://en.wikipedia.org/wiki/List_of_DNS_record_types#Resource_records
    """
    A = 1
    NS = 2
    CNAME = 5
    SOA = 6
    PTR = 12
    MX = 15
    TXT = 16
    AAAA = 28
    DS = 43
    DNSKEY = 48
    CDS = 59
    CDNSKEY = 60

    @classmethod
    def get(cls, query_type):
        """
        Returns the enum from a string or int
        """

        # We are already an enum so nothing more to do
        if isinstance(query_type, cls):
            return query_type

        # Try and find the enum by the string value
        try:
            return cls[query_type.upper()]
        except (KeyError, AttributeError):
            pass

        # Try and find the enum by record type id
        try:
            return cls(query_type)
        except ValueError:
            pass

        # This is the exception we raise if the query_type isn't valid
        raise InvalidQueryType(query_type)
