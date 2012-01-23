Summary:	Qt greeter for lightdm
Name:		lightdm-qt-greeter
Version:	1.1.1
Release:	0.1
License:	GPL v3
Group:		Themes
# no uploads yet
Source0:	lightdm-qt-greeter.tbz2
# Source0-md5:	887ef7022eb846e6d0f432d64f0bba69
URL:		https://launchpad.net/lightdm-qt-greeter
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	lightdm-devel >= 1.1.1-1
Provides:	lightdm-greeter
Obsoletes:	lightdm-greeter-qt < 1.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reference Qt greeter for LightDM.

%prep
%setup -qn %{name}

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/%{name}
%{_datadir}/xgreeters/%{name}.desktop
