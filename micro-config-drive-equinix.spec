Name     : micro-config-drive-equinix
Version  : 1
Release  : 2
Summary  : Start Equinix cloud-config user data helper at boot time
Group    : Development/Tools
License  : GPL-3.0
Requires: micro-config-drive

%description
A config-drive handler for Equinix.

%prep
%build
%check

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -sf ../ucd@.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/ucd@equinix.service

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/ucd@equinix.service

