BuildRequires: pkgconfig(blabla)
BuildRequires: pkg-config >= 2.2
Requires: pkgconfig(blabla)
%if %{with curses}
BuildRequires:  pkgconfig(ncurses)
%endif
