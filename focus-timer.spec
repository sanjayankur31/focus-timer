%global uuid pomodoro@arun.codito.in
%global forgeurl https://github.com/focustimerhq/FocusTimer

Version:        1.1.2

%global tag %{version}
%forgemeta

Epoch:          1
Name:           focus-timer
Release:        %autorelease
Summary:        A time-management app built around the Pomodoro Technique

License:        GPL-3.0-or-later
URL:            https://gnomepomodoro.org/
Source0:        %forgesource

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-controller-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(gtk4-x11)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(wayland-client)

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
Obsoletes:      gnome-pomodoro < 1:0.28.0-5

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
%forgesetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/io.github.focustimerhq.FocusTimer.desktop
appstreamcli validate --no-net %{buildroot}/%{_datadir}/metainfo/io.github.focustimerhq.FocusTimer.metainfo.xml

%files -f %{name}.lang
%doc README.md NEWS
%license COPYING
%{_bindir}/focus-timer
%{bash_completions_dir}/focus-timer
%{_datadir}/applications/io.github.focustimerhq.FocusTimer.desktop
%{_datadir}/dbus-1/interfaces/io.github.focustimerhq.FocusTimer*.xml
%{_datadir}/dbus-1/services/io.github.focustimerhq.FocusTimer.service
%{_datadir}/focus-timer/
%{_datadir}/glib-2.0/schemas/io.github.focustimerhq.FocusTimer*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/io.github.focustimerhq.FocusTimer*
%{_datadir}/knotifications6/io.github.focustimerhq.FocusTimer.notifyrc
%{_datadir}/metainfo/io.github.focustimerhq.FocusTimer.metainfo.xml

%changelog
%autochangelog
