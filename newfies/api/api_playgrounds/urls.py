#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#
from django.conf.urls import include, patterns
from api.api_playgrounds.phonebook_playground import PhonebookAPIPlayground
from api.api_playgrounds.campaign_playground import CampaignAPIPlayground
from api.api_playgrounds.callrequest_playground import CallrequestAPIPlayground
from api.api_playgrounds.voiceapp_playground import VoiceAppAPIPlayground
from api.api_playgrounds.bulk_contact_playground import BulkContactAPIPlayground
from api.api_playgrounds.campaign_delete_cascade_playground import \
    CampaignDelCascadeAPIPlayground
from api.api_playgrounds.campaign_subscriber_playground import \
    CampaignSubscriberAPIPlayground
from api.api_playgrounds.campaign_subscriber_per_campaign_playground import \
    CampaignSubscriberPerCampaignAPIPlayground
from api.api_playgrounds.dialcallback_playground import DialCallbackAPIPlayground
from api.api_playgrounds.store_cdr_playground import StoreCdrAPIPlayground
from api.api_playgrounds.answercall_playground import AnswerCallAPIPlayground
from api.api_playgrounds.hangupcall_playground import HangupCallAPIPlayground
from api.api_playgrounds.survey_playground import SurveyAPIPlayground
from api.api_playgrounds.section_playground import SectionAPIPlayground
from api.api_playgrounds.branching_playground import BranchingAPIPlayground


urlpatterns = patterns('',

    (r'explorer/voiceapp/', include(VoiceAppAPIPlayground().urls)),
    (r'explorer/phonebook/', include(PhonebookAPIPlayground().urls)),
    (r'explorer/bulk-contact/', include(BulkContactAPIPlayground().urls)),
    (r'explorer/campaign/', include(CampaignAPIPlayground().urls)),
    (r'explorer/campaign-delete-cascade/',
        include(CampaignDelCascadeAPIPlayground().urls)),
    (r'explorer/campaign-subscriber/',
        include(CampaignSubscriberAPIPlayground().urls)),
    (r'explorer/campaign-subscriber-per-campaign/',
        include(CampaignSubscriberPerCampaignAPIPlayground().urls)),
    (r'explorer/callrequest/', include(CallrequestAPIPlayground().urls)),
    (r'explorer/dialcallback/', include(DialCallbackAPIPlayground().urls)),
    (r'explorer/store_cdr/', include(StoreCdrAPIPlayground().urls)),
    (r'explorer/answercall/', include(AnswerCallAPIPlayground().urls)),
    (r'explorer/hangupcall/', include(HangupCallAPIPlayground().urls)),
    (r'explorer/survey/', include(SurveyAPIPlayground().urls)),
    (r'explorer/section/', include(SectionAPIPlayground().urls)),
    (r'explorer/branching/', include(BranchingAPIPlayground().urls)),

    # API list view
    (r'explorer/$', 'api.api_playgrounds.views.api_list_view'),
)
