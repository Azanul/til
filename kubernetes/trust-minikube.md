# How to add minikube cert to trusted certificates in your machine
-------------------------------------------------------------------

To obtain the CA certificate in Minikube, you can use the minikube ssh command to SSH into the Minikube VM 
and retrieve the certificate from the file system. Here are the steps to do this:

Start the Minikube cluster, if it's not already running, by running the following command:
```bash
minikube start
```

SSH into the Minikube VM by running the following command:
```bash
minikube ssh
```
Once you are logged into the Minikube VM, run the following command to retrieve the CA certificate:
```bash
cat /var/lib/minikube/certs/ca.crt
```

This will print the contents of the CA certificate to the console.
Copy the contents of the CA certificate and add it to your computer's trusted certificate store.

The steps to add the Kubernetes CA certificate to your computer's trusted certificate store depend on the operating system you are using.
Here are the steps for some common operating systems:

## MacOS
- Open the "Keychain Access" application.
- Click on the "System" keychain.
- Click on the "Certificates" category.
- Drag and drop the CA certificate file into the "Certificates" list.
- Double-click on the newly-added certificate in the list to open it.
- Expand the "Trust" section.
- Change the "When using this certificate" option to "Always Trust".
- Close the certificate window and enter your administrator password to save the changes.

## Linux
The steps to add a certificate to the trusted store vary depending on the Linux distribution and desktop environment you are using.
Here are the general steps:
- Copy the CA certificate file to the `/usr/local/share/ca-certificates/` directory.
- Run the following command to update the certificate store:
```bash
sudo update-ca-certificates
```

## Windows
- Open the Windows "Start" menu and search for "Manage computer certificates".
- Select "Trusted Root Certification Authorities" from the left-hand panel.
- Right-click on the "Certificates" folder and select "All Tasks" 
- Follow the wizard to import the CA certificate fill Tasks" -> "Import".
