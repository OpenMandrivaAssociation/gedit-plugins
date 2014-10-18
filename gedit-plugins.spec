%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_ld_no_undefined 1

Summary:	Extra plugins for gedit
Name:		gedit-plugins
Version:	3.14.0
Release:	1
License:	GPLv2+
Group:		Editors 
Url:		http://gedit.pn.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gedit-plugins/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	pkgconfig(gedit)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtksourceview-3.0)
BuildRequires:	pkgconfig(libpeas-gtk-1.0)
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
%configure 

%make

%install
%makeinstall_std

%find_lang gedit --with-gnome
%find_lang %{name}

cat %{name}.lang >> gedit.lang

%files -f gedit.lang
%doc COPYING AUTHORS
%{_libdir}/gedit/plugins/*
%{_datadir}/appdata/*
%{_datadir}/gedit/plugins/*
%{_datadir}/glib-2.0/schemas/*.xml
