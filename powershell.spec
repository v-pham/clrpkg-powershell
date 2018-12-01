Name:           powershell
Version:        6.1.1
Release:        0
Epoch:          1
Summary:        PowerShell is an automation and configuration management platform.
URL:            https://github.com/PowerShell/PowerShell
Source0:        https://github.com/PowerShell/PowerShell/releases/download/v%{version}/powershell-%{version}-linux-x64.tar.gz
License:        MIT

%description
PowerShell is an automation and configuration management platform.
It consists of a cross-platform command-line shell and associated scripting language.

%prep
%setup -q -c powershell-6.1.1 #unpack tarball

%build

%install
install -m 755 -d %{buildroot}/opt/microsoft/%{name}-%{version}
cp -rfa * %{buildroot}/opt/microsoft/%{name}-%{version}
mkdir -p %{buildroot}/usr/bin
ln -s opt/microsoft/%{name}-%{version}/pwsh %{buildroot}/usr/bin/pwsh
pushd %{buildroot}/
ln -s opt/microsoft/%{name}-%{version} opt/microsoft/%{name}
popd

%clean
rm -rf %{buildroot}

%post
#!/bin/sh
echo "/usr/bin/pwsh" >> /usr/share/defaults/etc/shells

%postun
if [ "$1" = 0 ] ; then
    TmpFile=`/bin/mktemp /tmp/.powershellmXXXXXX`
    grep -v '^/usr/bin/pwsh$' /usr/share/defaults/etc/shells > $TmpFile
    cp -f $TmpFile /usr/share/defaults/etc/shells
    rm -f $TmpFile
fi

%files
%defattr(-,root,root,-)
%dir %attr(0755,root,root) /opt 
%dir %attr(0755,root,root) /opt/microsoft
%dir %attr(0755,root,root) /opt/microsoft/%{name}-%{version}
/opt/microsoft/%{name}-%{version}/*
/opt/microsoft/%{name}
/usr/bin/pwsh
