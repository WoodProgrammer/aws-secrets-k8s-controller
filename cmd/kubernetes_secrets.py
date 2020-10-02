
from kubernetes import client, config, watch
CRD_DOMAIN = "woodprogrammer.cloudops.local"

class KubernetesSecrets(object):

    def __init__(self):
        if 'KUBERNETES_PORT' in os.environ:
            config.load_incluster_config()
        else:
            config.load_kube_config()

        configuration = client.Configuration()
        configuration.assert_hostname = False
        api_client = client.api_client.ApiClient(configuration=configuration)

    def createKubernetesSecrets(self, is_file):