Name:          xkb-tizen-data
Version:       0.0.1
Release:       0
BuildArch:     noarch
Summary:       Xkb data files
Group:         Graphics & UI Framework/Other
License:       MIT
Source0:       %{name}-%{version}.tar.gz
Source1001:    %{name}.manifest

%global TZ_SYS_RO_SHARE  %{?TZ_SYS_RO_SHARE:%TZ_SYS_RO_SHARE}%{!?TZ_SYS_RO_SHARE:/usr/share}

%description
Data files for Xkb keymap

%prep
%setup -q
cp -a %{SOURCE1001} .

%build
%autogen
%configure

make

%install
rm -rf %{buildroot}

# install service
%__mkdir_p %{buildroot}/%{TZ_SYS_RO_SHARE}/X11/xkb
%__cp -f xkb/tizen_key_layout.txt %{buildroot}/%{TZ_SYS_RO_SHARE}/X11/xkb/tizen_key_layout.txt
%__cp -f xkb/xkb.rule %{buildroot}/%{TZ_SYS_RO_SHARE}/X11/xkb/xkb.rule

# for license notification
mkdir -p %{buildroot}/%{TZ_SYS_RO_SHARE}/license
cp -a %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/%{TZ_SYS_RO_SHARE}/license/%{name}

%pre

%postun

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{TZ_SYS_RO_SHARE}/license/%{name}
%{TZ_SYS_RO_SHARE}/X11/xkb/tizen_key_layout.txt
%{TZ_SYS_RO_SHARE}/X11/xkb/xkb.rule
