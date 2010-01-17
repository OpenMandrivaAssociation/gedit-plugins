%define req_gedit_version 2.29.3
Summary:		Extra plugins for gedit
Name:			gedit-plugins
Version:		2.29.4
Release:		%mkrel 1
License:		GPLv2+
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
#gw pyvte.pc is in vte-devel
BuildRequires:	vte-devel
BuildRequires:  python-gtksourceview-devel
BuildRequires:  gtksourceview-devel >= 2.9.1
BuildRequires:	intltool
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


%preun
%_preun_uninstall_gconf_schemas gedit-show-tabbar-plugin gedit-drawspaces

%files -f %{gettext_package}.lang
%defattr(-, root, root)
%doc COPYING ChangeLog AUTHORS
%_sysconfdir/gconf/schemas/gedit-drawspaces.schemas
%_sysconfdir/gconf/schemas/gedit-show-tabbar-plugin.schemas
%{_libdir}/gedit-2/plugins/*.so
%{_libdir}/gedit-2/plugins/*.gedit-plugin
%{_libdir}/gedit-2/plugins/*.py*
%{_libdir}/gedit-2/plugins/commander/
%{_libdir}/gedit-2/plugins/multiedit
%{_libdir}/gedit-2/plugins/sessionsaver/
%{_datadir}/gedit-2/plugins/commander/
%{_datadir}/gedit-2/plugins/bookmarks
%{_datadir}/gedit-2/plugins/drawspaces/
%{_datadir}/gedit-2/plugins/sessionsaver/
