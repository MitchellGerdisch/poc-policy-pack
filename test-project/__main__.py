"""A Python Pulumi program"""

import pulumi
import pulumi_azuread as azuread

base_name = f"{pulumi.get_project()}-{pulumi.get_stack()}"
appreg = azuread.ApplicationRegistration("appreg",
                                         display_name=f"{base_name}-appreg",
)

redirect_uris = [
    "https://example.com",
    "https://jesslex.com",
    "https://localhost:8080",
    "http://localhost:8000",
    "https://127.0.0.1:443",
    "http://127.0.0.1:80",
]
appredirect = azuread.ApplicationRedirectUris("appredirect",
    application_id=appreg.id,
    redirect_uris=redirect_uris,
    type="Web",
)
