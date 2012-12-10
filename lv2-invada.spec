Summary:	Invada Studio audio plugins
Name:		lv2-invada
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	https://launchpad.net/invada-studio/lv2/1.2/+download/invada-studio-plugins-lv2_%{version}-nopkg.tgz
# Source0-md5:	fe05214dd65dd3096d03c91d05bc3f5d
Patch0:		%{name}-lv2-spec-update.patch
BuildRequires:	gtk+-devel
BuildRequires:	libglade-devel
BuildRequires:	lv2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of LV2 audio plugins.

%prep
%setup -qn invada-studio-plugins-lv2-%{version}
%patch0 -p1

# use rpmcflags
find . -name Makefile -print | xargs %{__sed} -i "s/-O3/%{rpmcflags}/g"

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-sys \
	DESTDIR=$RPM_BUILD_ROOT	\
	INSTALL_SYS_PLUGINS_DIR=%{_libdir}/lv2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/lv2/invada.lv2
%attr(755,root,root) %{_libdir}/lv2/invada.lv2/*.so
%{_libdir}/lv2/invada.lv2/*.ttl
%{_libdir}/lv2/invada.lv2/gtk

