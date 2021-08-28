%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE Panel applet indicator
Name:		mate-indicator-applet
Version:	1.26.0
Release:	1
License:	LGPLv2+ GPLv3
Group:		Graphical desktop/Other
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool

BuildRequires:	autoconf-archive
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(indicator3-0.4)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)
BuildRequires:	pkgconfig(x11)

Requires:	mate-panel

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides a small applet to display information from various
applications consistently in the panel.

The indicator applet exposes Ayatana Indicators in the MATE Panel. Ayatana
Indicators are an initiative by Canonical to provide crisp and clean system
and application status indication. They take the form of an icon and
associated menu, displayed (usually) in the desktop panel. Existing
indicators include the Message Menu, Battery Menu and Sound menu.

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libexecdir}/mate-indicator-applet*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/mate-panel/applets/*.mate-panel-applet
%{_iconsdir}/hicolor/*/*/*

#---------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
#NOCONFIGURE=yes ./autogen.sh
%configure
%make_build

%install
%make_install

# locales
%find_lang %{name} --with-gnome --all-name

