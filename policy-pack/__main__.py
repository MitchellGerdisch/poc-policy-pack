from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

## Policy to ensure app registrations do not have localhost or 127.0.0.1 in the redirect URI
def check_appregistration_no_redirect_to_localhost(args: ResourceValidationArgs, report_violation: ReportViolation):
    ## Handy way to see what the resource looks like to make sure we are looking for the right value.
    ## print(f"Checking resource type: {args.resource_type}")
    if args.resource_type == "azuread:index/applicationRedirectUris:ApplicationRedirectUris":
        ## Note that even though this policy is in Python, camel cae is used for the property names.
        redirect_uris = args.props["redirectUris"]
        bad_redirect_dests = ["localhost", "127.0.0.1"]
        bad_redirects_found = []
        for redirect_uri in redirect_uris:
            for bad_redirect_dest in bad_redirect_dests:
                if bad_redirect_dest in redirect_uri:
                    bad_redirects_found.append(redirect_uri)

        if len(bad_redirects_found) > 0:
            report_violation(
                f"App Registration redirect URI, {args.name}, must not contain localhost or 127.0.0.1.\nFound these bad redirect URIs: {bad_redirects_found}",
            )


appregistration_no_redirect_to_localhost = ResourceValidationPolicy(
    name="appregistration_no_redirect_to_localhost",
    description="Prohibits having App Redirects to localhost or equivalent addresses.",
    validate=check_appregistration_no_redirect_to_localhost,
)

PolicyPack(
    name="poc-python",
    enforcement_level=EnforcementLevel.ADVISORY, ## Can change to MANDATORY in Pulumi Cloud
    policies=[
        appregistration_no_redirect_to_localhost
    ],
)