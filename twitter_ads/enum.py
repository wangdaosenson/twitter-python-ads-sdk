# Copyright (C) 2015 Twitter, Inc.

"""Container for all enum values used by the Ads API SDK."""


def enum(**enums):
    return type('Enum', (), enums)

TRANSFORM = enum(
    TIME=0,
    BOOL=1,
    INT=2,
    LIST=3,
    OBJECT=4
)

APPROVAL_STATUS = enum(
    ACCEPTED='ACCEPTED',
    UNDER_REVIEW='UNDER_REVIEW',
    REJECTED='REJECTED'
)

BID_UNIT = enum(
    APP_CLICK='APP_CLICK',
    APP_INSTALL='APP_INSTALL',
    ENGAGEMENT='ENGAGEMENT',
    FOLLOW='FOLLOW',
    LEAD='LEAD',
    LINK_CLICK='LINK_CLICK',
    VIEW='VIEW'
)

CHARGE_BY = enum(
    APP_CLICK='APP_CLICK',
    APP_INSTALL='APP_INSTALL',
    ENGAGEMENT='ENGAGEMENT',
    FOLLOW='FOLLOW',
    LEAD='LEAD',
    LINK_CLICK='LINK_CLICK',
    VIEW='VIEW'
)

OPTIMIZATIONS = enum(
    DEFAULT='DEFAULT',
    WEBSITE_CONVERSIONS='WEBSITE_CONVERSIONS'
)

PRODUCT = enum(
    PROMOTED_ACCOUNT='PROMOTED_ACCOUNT',
    PROMOTED_TWEETS='PROMOTED_TWEETS',
    MEDIA='MEDIA',
    LIVE_TV_EVENT='LIVE_TV_EVENT'
)

PLACEMENT = enum(
    ALL_ON_TWITTER='ALL_ON_TWITTER',
    TWITTER_SEARCH='TWITTER_SEARCH',
    TWITTER_TIMELINE='TWITTER_TIMELINE',
    PUBLISHER_NETWORK='PUBLISHER_NETWORK',
    TWITTER_PROFILE='TWITTER_PROFILE'
)

OBJECTIVE = enum(
    APP_ENGAGEMENTS='APP_ENGAGEMENTS',
    APP_INSTALLS='APP_INSTALLS',
    FOLLOWERS='FOLLOWERS',
    LEAD_GENERATION='LEAD_GENERATION',
    TWEET_ENGAGEMENTS='TWEET_ENGAGEMENTS',
    VIDEO_VIEWS_PREROLL='VIDEO_VIEWS_PREROLL',
    VIDEO_VIEWS='VIDEO_VIEWS',
    WEBSITE_CLICKS='WEBSITE_CLICKS',
    WEBSITE_CONVERSIONS='WEBSITE_CONVERSIONS'
)

GRANULARITY = enum(
    HOUR='HOUR',
    DAY='DAY',
    TOTAL='TOTAL'
)

AGE_BUCKET = enum(
    AGE_13_TO_17='AGE_13_TO_17',
    AGE_18_TO_24='AGE_18_TO_24',
    AGE_25_TO_34='AGE_25_TO_34',
    AGE_35_TO_44='AGE_35_TO_44',
    AGE_45_TO_54='AGE_45_TO_54',
    AGE_55_TO_64='AGE_55_TO_64',
    AGE_OVER_65='AGE_OVER_65'
)

AGE_BUCKET_COARSE = enum(
    AGE_18_TO_34='AGE_18_TO_34',
    AGE_18_TO_49='AGE_18_TO_49',
    AGE_25_TO_54='AGE_25_TO_54',
    AGE_OVER_21='AGE_OVER_21'
)

EVENTS = enum(
    MUSIC_AND_ENTERTAINMENT='MUSIC_AND_ENTERTAINMENT',
    SPORTS='SPORTS',
    HOLIDAY='HOLIDAY',
    CONFERENCE='CONFERENCE',
    OTHER='OTHER'
)

TA_LIST_TYPES = enum(
    EMAIL='EMAIL',
    DEVICE_ID='DEVICE_ID',
    TWITTER_ID='TWITTER_ID',
    HANDLE='HANDLE',
    PHONE_NUMBER='PHONE_NUMBER'
)

TA_OPERATIONS = enum(
    ADD='ADD',
    REMOVE='REMOVE',
    REPLACE='REPLACE'
)

PERMISSION_LEVEL = enum(
    READ_ONLY='READ_ONLY',
    READ_WRITE='READ_WRITE'
)

# Analytics v1
METRIC_GROUP = enum(
    ENGAGEMENT='ENGAGEMENT',
    WEB_CONVERSION='WEB_CONVERSION',
    MOBILE_CONVERSION='MOBILE_CONVERSION',
    MEDIA='MEDIA',
    VIDEO='VIDEO',
    BILLING='BILLING',
    LIFE_TIME_VALUE_MOBILE_CONVERSION='LIFE_TIME_VALUE_MOBILE_CONVERSION'
)

JOB_STATUS = enum(
    QUEUED='QUEUED',
    PROCESSING='PROCESSING',
    UPLOADING='UPLOADING',
    SUCCESS='SUCCESS',
    FAILED='FAILED'
)

ENTITY = enum(
    ACCOUNT='ACCOUNT',
    FUNDING_INSTRUMENT='FUNDING_INSTRUMENT',
    CAMPAIGN='CAMPAIGN',
    LINE_ITEM='LINE_ITEM',
    PROMOTED_TWEET='PROMOTED_TWEET',
    ORGANIC_TWEET='ORGANIC_TWEET'
)

# Tweet
TWEET_MODE = enum(
    compat='compat',
    extended='extended',
    COMPAT='compat',
    EXTENDED='extended'
)

# TA Memberships
MEMBERSHIP_TYPE = enum(
    WEB_MEMBERSHIP='WEB_MEMBERSHIP',
    WEB_OPTOUT='WEB_OPTOUT',
    LIST_MEMBERSHIP='LIST_MEMBERSHIP'
)

USER_IDENTIFIER_TYPE = enum(
    TALIST_PARTNER_USER_ID='TALIST_PARTNER_USER_ID',
    TAWEB_PARTNER_USER_ID='TAWEB_PARTNER_USER_ID',
    EMAIL='EMAIL',
    HANDLE='HANDLE',
    TWITTER_ID='TWITTER_ID',
    DEVICE_ID='DEVICE_ID',
    PHONE_NUMBER='PHONE_NUMBER'
)

# Creatives
CREATIVES = enum(
    BANNER='BANNER',
    INTERSTITIAL='INTERSTITIAL',
    PREROLL='PREROLL',
    VAST_PREROLL='VAST_PREROLL'
)
