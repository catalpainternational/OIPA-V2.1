from django_filters import FilterSet, NumberFilter, DateFilter, BooleanFilter
from api.generics.filters import CommaSeparatedCharFilter
from api.generics.filters import CommaSeparatedStickyCharFilter
from api.generics.filters import ToManyFilter
from api.generics.filters import ToManyNotInFilter

from api.activity.filters import ActivityFilter

from iati.models import *
from iati.transaction.models import *

class TransactionFilter(FilterSet):
    """
    Transaction filter class
    """

    transaction_type = CommaSeparatedCharFilter(
        name='transaction_type',
        lookup_expr='in')

    currency = CommaSeparatedCharFilter(
        name='currency',
        lookup_expr='in')

    transaction_date_year = NumberFilter(
        lookup_expr='year',
        name='transaction_date'
    )

    transaction_date_lte = DateFilter(
        lookup_expr='lte',
        name='transaction_date')

    transaction_date_gte = DateFilter(
        lookup_expr='gte',
        name='transaction_date')


    min_value = NumberFilter(name='value', lookup_expr='gte')
    max_value = NumberFilter(name='value', lookup_expr='lte')
    
    value_not = NumberFilter(lookup_expr='exact', name='value', exclude=True)
    xdr_value_not = NumberFilter(lookup_expr='exact', name='xdr_value', exclude=True)
    usd_value_not = NumberFilter(lookup_expr='exact', name='usd_value', exclude=True)
    eur_value_not = NumberFilter(lookup_expr='exact', name='eur_value', exclude=True)
    gbp_value_not = NumberFilter(lookup_expr='exact', name='gbp_value', exclude=True)
    jpy_value_not = NumberFilter(lookup_expr='exact', name='jpy_value', exclude=True)
    cad_value_not = NumberFilter(lookup_expr='exact', name='cad_value', exclude=True)

    provider_activity = ToManyFilter(
        qs=TransactionProvider,
        lookup_expr='in',
        name='provider_activity_ref',
        fk='transaction',
    )

    has_provider_activity = BooleanFilter(
        name='provider_organisation__provider_activity',
        lookup_expr='isnull',
        exclude=True)

    provider_activity_reporting_org = ToManyFilter(
        qs=TransactionProvider,
        lookup_expr='in',
        name='provider_activity__reporting_organisations__organisation__organisation_identifier',
        fk='transaction',
    )

    provider_organisation_primary_name = ToManyFilter(
        qs=TransactionProvider,
        lookup_expr='in',
        name='primary_name',
        fk='transaction',
    )

    provider_organisation_name = ToManyFilter(
        qs=TransactionProvider,
        lookup_expr='in',
        name='narratives__content',
        fk='transaction',
    )

    receiver_organisation_primary_name = ToManyFilter(
        qs=TransactionReceiver,
        lookup_expr='in',
        name='primary_name',
        fk='transaction',
    )

    receiver_organisation_name = ToManyFilter(
        qs=TransactionReceiver,
        lookup_expr='in',
        name='narratives__content',
        fk='transaction',
    )

    #
    # Activity filters...
    #

    activity_id = CommaSeparatedCharFilter(
        name='activity__id',
        lookup_expr='in')

    iati_identifier = CommaSeparatedCharFilter(
        name='activity__iati_identifier',
        lookup_expr='in')

    activity_scope = CommaSeparatedCharFilter(
        name='activity__scope__code',
        lookup_expr='in',)

    planned_start_date_lte = DateFilter(
        lookup_expr='lte',
        name='activity__planned_start')

    planned_start_date_gte = DateFilter(
        lookup_expr='gte',
        name='activity__planned_start')

    actual_start_date_lte = DateFilter(
        lookup_expr='lte',
        name='activity__actual_start')

    actual_start_date_gte = DateFilter(
        lookup_expr='gte',
        name='activity__actual_start')

    planned_end_date_lte = DateFilter(
        lookup_expr='lte',
        name='activity__planned_end')

    planned_end_date_gte = DateFilter(
        lookup_expr='gte',
        name='activity__planned_end')

    actual_end_date_lte = DateFilter(
        lookup_expr='lte',
        name='activity__actual_end')

    actual_end_date_gte = DateFilter(
        lookup_expr='gte',
        name='activity__actual_end')

    end_date_lte = DateFilter(
        lookup_expr='lte',
        name='activity__end_date')

    end_date_gte = DateFilter(
        lookup_expr='gte',
        name='activity__end_date')

    start_date_lte = DateFilter(
        lookup_expr='lte',
        name='activity__start_date')

    start_date_gte = DateFilter(
        lookup_expr='gte',
        name='activity__start_date')

    end_date_isnull = BooleanFilter(name='activity__end_date__isnull')
    start_date_isnull = BooleanFilter(name='activity__start_date__isnull')

    activity_status = CommaSeparatedCharFilter(
        lookup_expr='in',
        name='activity__activity_status',)

    document_link_category = ToManyFilter(
        main_fk='activity',
        qs=DocumentLink,
        fk='activity',
        lookup_expr='in',
        name='categories__code',
    )

    hierarchy = CommaSeparatedCharFilter(
        lookup_expr='in',
        name='activity__hierarchy',)

    collaboration_type = CommaSeparatedCharFilter(
        lookup_expr='in',
        name='activity__collaboration_type',)

    default_flow_type = CommaSeparatedCharFilter(
        lookup_expr='in',
        name='activity__default_flow_type',)

    default_aid_type = CommaSeparatedCharFilter(
        lookup_expr='in',
        name='activity__default_aid_type',)

    default_finance_type = CommaSeparatedCharFilter(
        lookup_expr='in',
        name='activity__default_finance_type',)

    default_tied_status = CommaSeparatedCharFilter(
        lookup_expr='in',
        name='activity__default_tied_status',)

    budget_period_start = DateFilter(
        lookup_expr='gte',
        name='activity__budget__period_start',)

    budget_period_end = DateFilter(
        lookup_expr='lte',
        name='activity__budget__period_end')

    related_activity_id = ToManyFilter(
        main_fk='activity',
        qs=RelatedActivity,
        fk='current_activity',
        lookup_expr='in',
        name='ref_activity__iati_identifier',
    )

    related_activity_type = ToManyFilter(
        main_fk='activity',
        qs=RelatedActivity,
        lookup_expr='in',
        name='type__code',
        fk='current_activity',
    )

    related_activity_recipient_country = ToManyFilter(
        main_fk='activity',
        qs=RelatedActivity,
        lookup_expr='in',
        name='ref_activity__recipient_country',
        fk='current_activity',
    )

    related_activity_recipient_region = ToManyFilter(
        main_fk='activity',
        qs=RelatedActivity,
        lookup_expr='in',
        name='ref_activity__recipient_region',
        fk='current_activity',
    )

    related_activity_sector = ToManyFilter(
        main_fk='activity',
        qs=RelatedActivity,
        lookup_expr='in',
        name='ref_activity__sector',
        fk='current_activity',
    )

    related_activity_sector_category = ToManyFilter(
        main_fk='activity',
        qs=RelatedActivity,
        lookup_expr='in',
        name='ref_activity__sector__category',
        fk='current_activity',
    )

    budget_currency = ToManyFilter(
        main_fk='activity',
        qs=Budget,
        lookup_expr='in',
        name='currency__code',
        fk='activity',
    )

    # makes no
    # TO DO: check if this also influences other filters
    # for example, sector_category should probably filter through transactionsector__sector__category 
    # in the transaction endpoint 

    recipient_country = ToManyFilter(
        main_fk='activity',
        qs=ActivityRecipientCountry,
        lookup_expr='in',
        name='country__code',
        fk='activity',
    )

    recipient_region = ToManyFilter(
        main_fk='activity',
        qs=ActivityRecipientRegion,
        lookup_expr='in',
        name='region__code',
        fk='activity',
    )

    recipient_region_not = ToManyNotInFilter(
        main_fk='activity',
        qs=ActivityRecipientRegion,
        lookup_expr='in',
        name='region__code',
        fk='activity',
    )

    sector = ToManyFilter(
        main_fk='activity',
        qs=ActivitySector,
        lookup_expr='in',
        name='sector__code',
        fk='activity',
    )

    sector_startswith = ToManyFilter(
        qs=ActivitySector,
        lookup_expr='startswith',
        name='sector__code',
        fk='activity',
    )

    sector_vocabulary = ToManyFilter(
        main_fk='activity',
        qs=ActivitySector,
        lookup_expr='in',
        name='sector__vocabulary__code',
        fk='activity',
    )

    transaction_recipient_country = ToManyFilter(
        qs=TransactionRecipientCountry,
        lookup_expr='in',
        name='country__code',
        fk='transaction',
    )

    transaction_recipient_region = ToManyFilter(
        qs=TransactionRecipientRegion,
        lookup_expr='in',
        name='region__code',
        fk='transaction',
    )

    transaction_sector = ToManyFilter(
        qs=TransactionSector,
        lookup_expr='in',
        name='sector__code',
        fk='transaction',
    )

    sector_category = ToManyFilter(
        main_fk='activity',
        qs=ActivitySector,
        lookup_expr='in',
        name='sector__category__code',
        fk='activity',
    )

    participating_organisation_ref = ToManyFilter(
        main_fk='activity',
        qs=ActivityParticipatingOrganisation,
        lookup_expr='in',
        name='normalized_ref',
        fk='activity',
    )

    participating_organisation_name = ToManyFilter(
        main_fk='activity',
        qs=ActivityParticipatingOrganisation,
        lookup_expr='in',
        name='primary_name',
        fk='activity',
    )

    participating_organisation_role = ToManyFilter(
        main_fk='activity',
        qs=ActivityParticipatingOrganisation,
        lookup_expr='in',
        name='role__code',
        fk='activity',
    )

    participating_organisation_type = ToManyFilter(
        main_fk='activity',
        qs=ActivityParticipatingOrganisation,
        lookup_expr='in',
        name='type__code',
        fk='activity',
    )

    reporting_organisation_identifier = ToManyFilter(
        main_fk='activity',
        qs=ActivityReportingOrganisation,
        lookup_expr='in',
        name='organisation__organisation_identifier',
        fk='activity',
    )

    result_title = ToManyFilter(
        main_fk='activity',
        qs=Result,
        lookup_expr='in',
        name='resulttitle__narratives__content',
        fk='activity',
    )

    reporting_organisation_identifier_startswith = ToManyFilter(
        main_fk='activity',
        qs=ActivityReportingOrganisation,
        lookup_expr='startswith',
        name='organisation__organisation_identifier',
        fk='activity',
    )



    # activity aggregation filters
    total_budget_lte = NumberFilter(
        lookup_expr='lte',
        name='activity__activity_aggregation__budget_value')

    total_budget_gte = NumberFilter(
        lookup_expr='gte',
        name='activity__activity_aggregation__budget_value')

    total_disbursement_lte = NumberFilter(
        lookup_expr='lte',
        name='activity__activity_aggregation__disbursement_value')

    total_disbursement_gte = NumberFilter(
        lookup_expr='gte',
        name='activity__activity_aggregation__disbursement_value')

    total_incoming_funds_lte = NumberFilter(
        lookup_expr='lte',
        name='activity__activity_aggregation__incoming_funds_value')

    total_incoming_funds_gte = NumberFilter(
        lookup_expr='gte',
        name='activity__activity_aggregation__incoming_funds_value')

    total_expenditure_lte = NumberFilter(
        lookup_expr='lte',
        name='activity__activity_aggregation__expenditure_value')

    total_expenditure_gte = NumberFilter(
        lookup_expr='gte',
        name='activity__activity_aggregation__expenditure_value')

    total_commitment_lte = NumberFilter(
        lookup_expr='lte',
        name='activity__activity_aggregation__commitment_value')

    total_commitment_gte = NumberFilter(
        lookup_expr='gte',
        name='activity__activity_aggregation__commitment_value')

    total_hierarchy_budget_lte = NumberFilter(
        lookup_expr='lte',
        name='activity__activity_plus_child_aggregation__budget_value')

    total_hierarchy_budget_gte = NumberFilter(
        lookup_expr='gte',
        name='activity__activity_plus_child_aggregation__budget_value')

    total_hierarchy_disbursement_lte = NumberFilter(
        lookup_expr='lte',
        name='activity__activity_plus_child_aggregation__disbursement_value')

    total_hierarchy_disbursement_gte = NumberFilter(
        lookup_expr='gte',
        name='activity__activity_plus_child_aggregation__disbursement_value')

    total_hierarchy_incoming_funds_lte = NumberFilter(
        lookup_expr='lte',
        name='activity__activity_plus_child_aggregation__incoming_funds_value')

    total_hierarchy_incoming_funds_gte = NumberFilter(
        lookup_expr='gte',
        name='activity__activity_plus_child_aggregation__incoming_funds_value')

    total_hierarchy_expenditure_lte = NumberFilter(
        lookup_expr='lte',
        name='activity__activity_plus_child_aggregation__expenditure_value')

    total_hierarchy_expenditure_gte = NumberFilter(
        lookup_expr='gte',
        name='activity__activity_plus_child_aggregation__expenditure_value')

    total_hierarchy_commitment_lte = NumberFilter(
        lookup_expr='lte',
        name='activity__activity_plus_child_aggregation__commitment_value')

    total_hierarchy_commitment_gte = NumberFilter(
        lookup_expr='gte',
        name='activity__activity_plus_child_aggregation__commitment_value')


    class Meta:
        model = Transaction
        fields = [
            'id',
            'aid_type',
            'transaction_type',
            'value',
            'min_value',
            'max_value',
        ]


class TransactionAggregationFilter(TransactionFilter):
    """
    Transaction aggregation filter class
    """

    recipient_country = CommaSeparatedStickyCharFilter(
        name='transactionrecipientcountry__country__code',
        lookup_expr='in',
    )

    recipient_region = CommaSeparatedStickyCharFilter(
        name='transactionrecipientregion__region__code',
        lookup_expr='in',
    )

    sector = CommaSeparatedStickyCharFilter(
        name='transactionsector__sector__code',
        lookup_expr='in',
    )

    sector_vocabulary = CommaSeparatedStickyCharFilter(
        name='transactionsector__sector__vocabulary__code',
        lookup_expr='in',
    )

    transaction_recipient_country = CommaSeparatedStickyCharFilter(
        name='transactionrecipientcountry__country__code',
        lookup_expr='in',
    )

    transaction_recipient_region = CommaSeparatedStickyCharFilter(
        name='transactionrecipientregion__region__code',
        lookup_expr='in',
    )

    transaction_sector = CommaSeparatedStickyCharFilter(
        name='transactionsector__sector__code',
        lookup_expr='in',
    )

    policy_marker = CommaSeparatedStickyCharFilter(
        name='activity__activitypolicymarker__code',
        lookup_expr='in',
    )

    policy_marker_significance = CommaSeparatedStickyCharFilter(
        name='activity__activitypolicymarker__significance',
        lookup_expr='in',
    )

