%define req_gedit_version 2.16
Summary:		Extra plugins for gedit
Name:			gedit-plugins
Version:		2.20.0
Release:		%mkrel 2
License:		GPL
Group:			Editors 
Source0:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
URL:			http://gedit.pn.org/
BuildRoot:		%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	pygtk2.0-devel
BuildRequires:	gnome-python-desktop
BuildRequires:	libgnomeui2-devel
BuildRequires:  gedit-devel >= %{req_gedit_version}
BuildRequires:  gnome-doc-utils
BuildRequires:	gucharmap-devel
BuildRequires:	python-vte
BuildRequires:  python-gtksourceview-devel
Requires:	gedit >= %{req_gedit_version}
Requires:	python-vte

%description
gEdit is a small but powerful text editor designed expressly
for GNOME.

It includes such features as split-screen mode, a plugin
API, which allows gEdit to be extended to support many
features while remaining small at its core, multiple
document editing through the use of a 'tabbed' notebook and
many more functions.

This package contains some extra plugins for gEdit, extending gEdit
functionality.

%prep
%setup -q

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

# remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_libdir}/gedit-2/plugins/*.la

%define gettext_package %{name}
%{find_lang} %{gettext_package}

%clean
rm -rf $RPM_BUILD_ROOT

%post
GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/gedit-show-tabbar-plugin.schemas > /dev/null

%preun
if [ "$1" = "0" ] ; then
 GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/gedit-show-tabbar-plugin.schemas > /dev/null
fi

%files -f %{gettext_package}.lang
%defattr(-, root, root)
%doc COPYING ChangeLog AUTHORS
%_sysconfdir/gconf/schemas/gedit-show-tabbar-plugin.schemas
%{_libdir}/gedit-2/plugins/*.glade
%{_libdir}/gedit-2/plugins/*.so
%{_libdir}/gedit-2/plugins/*.gedit-plugin
%{_libdir}/gedit-2/plugins/*.py*
%{_libdir}/gedit-2/plugins/sessionsaver/
