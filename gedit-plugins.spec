Summary:	Extra plugins for gedit
Name:		gedit-plugins
Version:	3.4.0
Release:	1
License:	GPLv2+
Group:		Editors 
URL:		http://gedit.pn.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

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
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std
find %{buildroot} -name *.la | xargs rm

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING ChangeLog AUTHORS
%{_datadir}/glib-2.0/schemas/*.xml
%{_libdir}/gedit/plugins/*
%{_datadir}/gedit/plugins/*

