%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_ld_no_undefined 1
%define _disable_rebuild_configure 1

Summary:	Extra plugins for gedit
Name:		gedit-plugins
Version:	3.34.1
Release:	1
License:	GPLv2+
Group:		Editors 
Url:		http://gedit.pn.org/
Source0:	ftp://ftp.gnome.org:21/pub/GNOME/sources/gedit-plugins/3.14/%{name}-%{version}.tar.xz

BuildRequires:  appstream-util
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:  libxml2-utils
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	pkgconfig(gedit)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)
BuildRequires:  pkgconfig(vapigen)
Requires:	gedit >= %{version}

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
%meson
%meson_install

%install
%meson_install

%find_lang gedit --with-gnome
%find_lang %{name}

cat %{name}.lang >> gedit.lang

%files -f gedit.lang
%doc AUTHORS NEWS README
%{_datadir}/glib-2.0/schemas/*.xml
%{_libdir}/gedit/plugins/*
%{_datadir}/gedit/plugins/*
%{_metainfodir}/gedit-*.metainfo.xml
