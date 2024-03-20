# ansible-playbook-for-cp4i
Playbooks to Install/Remove Cloud Pak for Integration

The general purpose of these playbooks is to facilitate the process of installing Cloud Pak for Integration from a blank cluster to getting the Platform Navigator running where you can install instances of capabilities like MQ, ACE, etc. 

### Code Structure

All the individual playbooks are in the **playbooks** folder.  Inside the Playbooks folder, you will see an **artifacts** with version numbers that correspond to Cloud Pak for Integration. 

### Getting Started


1.  To get started, you will need to first copy for **vars_deployment_template.yaml** to be **vars_deployment.yaml**. 

2. Update **entitlement key** in the **vars_deployment.yaml** file. 

### Playbook Order

| Playbook  |   | Notes  |
|:----------|:----------|:----------|
| 01-namespace.yaml    |      | Creates general namespace from vars_deployment to centralize install for tools    |
| 01a-entitlement-key.yaml   |      | Iterative playbook to create entitlement key in a namspace ( if namespace does not exists, it will create it )   |
| 02-catalog-sources.yaml   |      | Installs all the declarative catalog sources for cloud pak version    |
| 02a-certmanager.yaml   |    | Installs the RH Certificate Manager in namespace    |
| 02b-subscriptions.yaml  |      | Activates instances of operators clusterwide.  ( you can manually install operators from Operator Hub as well )   |
| 04a-platform-navigator.yaml    |    | Installs instance of Platform Navigator with 3 replicas for ODF  |
| 04a-platform-navi-credentails.yaml    |    | Pulls Credentails for initial login for Platform Navigators  |

 

