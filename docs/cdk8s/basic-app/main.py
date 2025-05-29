#!/usr/bin/env python
from cdk8s import App, Chart
from constructs import Construct
from imports import k8s


class MyChart(Chart):
   def __init__(self, scope: Construct, ns: str, app_label: str):
       super().__init__(scope, ns)

       # Define a Kubernetes Deployment
       k8s.KubeDeployment(self, "my-deployment",
                       spec=k8s.DeploymentSpec(
                           replicas=3,
                           selector=k8s.LabelSelector(match_labels={"app": app_label}),
                           template=k8s.PodTemplateSpec(
                               metadata=k8s.ObjectMeta(labels={"app": app_label}),
                               spec=k8s.PodSpec(containers=[
                                   k8s.Container(
                                       name="app-container",
                                       image="nginx:1.19.10", # Using public nginx image
                                       ports=[k8s.ContainerPort(container_port=80)] # Nginx listens on port 80 by default
                                   )
                               ])
                           )
                       )
                   )

app = App()
MyChart(app, "getting-started", app_label="my-app")

app.synth()