%global forgeurl https://github.com/focustimerhq/FocusTimer

Version:        1.1.2

%global tag %{version}
%forgemeta

Epoch:          1
Name:           focustimer
Release:        %autorelease
Summary:        Work with regular breaks

License:        GPL-3.0-or-later
URL:            https://github.com/focustimerhq/FocusTimer
Source0:        %forgesource

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
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
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(wayland-client)

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
A productivity timer that helps you work more effectively by breaking your time into focused work sessions followed by short breaks.
Work for 25 minutes, then take a 5-minute break to maintain concentration and prevent burnout.

%prep
%forgesetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang focus-timer

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/io.github.focustimerhq.FocusTimer.desktop
appstreamcli validate --no-net %{buildroot}/%{_datadir}/metainfo/io.github.focustimerhq.FocusTimer.metainfo.xml

%files -f focus-timer.lang
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
