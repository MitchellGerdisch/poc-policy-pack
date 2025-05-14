# poc-policy-pack
A policy pack for a POC.

## Notes on how this was created
* `pulumi policy new azure-python` to get an initial skeleton for the policy pack.
* Edited `__main__.py` to have the desired policy logic.

## Notes on how to use
* `pulumi up --policy-pack PATH_TO_THIS_FOLDER --policy-config=` to test locally.
* `pulumi policy publish ORGNAME` to push the policy pack to a given Pulumi Cloud org.
*  ... tbd ... setting and pushing config if applicable
