%global uuid pomodoro@arun.codito.in

Epoch:          1
Name:           focus-timer
Version:        1.1.2
Release:        %autorelease
Summary:        A time management utility for GNOME

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://gnomepomodoro.org/
Source0:        https://github.com/focustimerhq/FocusTimer/archive/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(json-glib-1.0)

# For gnome shell extension part of gnome-pomodoro
Requires:       gnome-shell >= 40.0
Requires:       hicolor-icon-theme
# For /usr/share/dbus-1/services ownership
Requires:       dbus-common

# Provides/Obsoletes added in F35 due to package rename
Provides:       gnome-shell-extension-pomodoro = %{epoch}:%{version}-%{release}
Obsoletes:      gnome-shell-extension-pomodoro < 1:0.19.2-1

# Renamed upstream
Provides:       gnome-pomodoro = %{epoch}:%{version}-%{release}
Obsoletes:      gnome-pomodoro < 1:0.28.0-1

%description
This GNOME app helps to manage time according to Pomodoro Technique. It intends
to improve productivity and quality of work by reminding you to take short
breaks.

Pomodoro Technique is based on two principles:

- focusing on work for limited time, about half an hour,
- clearing your mind during breaks.

This workflow can improve focus, physical health and mental agility depending
on how you spend your breaks and how strictly you follow the routine.

%prep
%autosetup -n FocusTimer-%{version}

%build
%meson
%meson_build

%install
%meson_install

# Remove unneeded unversioned symlink
rm %{buildroot}%{_libdir}/lib%{name}.so

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Pomodoro.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/*/org.gnome.Pomodoro.appdata.xml

%files -f %{name}.lang
%doc README.md NEWS
%license COPYING
%{_bindir}/gnome-pomodoro
%{_libdir}/gnome-pomodoro
%{_libdir}/libgnome-pomodoro.so*
%{_datadir}/gnome-pomodoro
%{_datadir}/*/org.gnome.Pomodoro.appdata.xml
%{_datadir}/applications/org.gnome.Pomodoro.desktop
%{_datadir}/gnome-shell/extensions/%{uuid}/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/glib-2.0/schemas/org.gnome.pomodoro.*
%{_datadir}/dbus-1/services/org.gnome.Pomodoro.service

%changelog
%autochangelog
