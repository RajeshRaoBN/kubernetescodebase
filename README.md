# kubernetescodebase
Kubernetes Code Base

To create an encrypted user name and password use the following on the terminal.

% echo -n 'username' | base64
dXNlcm5hbWU=

% echo -n 'password' | base64
cGFzc3dvcmQ=

This can be used in secret file