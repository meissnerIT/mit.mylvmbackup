#
# spec file for package mylvmbackup (Version 0.16)
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

Name: mylvmbackup
Summary: Utility for creating MySQL backups via LVM snapshots
Version: 0.16
Release: 0
License: GPL
Group: Productivity/Archiving/Backup
Source: %{name}-%{version}.tar.gz
URL: http://www.lenzg.net/mylvmbackup/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch

%description
mylvmbackup is a script for quickly creating backups of MySQL server's data
files. To perform a backup, mylvmbackup obtains a read lock on all tables and
flushes all server caches to disk, makes an LVM snapshot of the volume
containing the MySQL data directory, and unlocks the tables again. The snapshot
process takes only a small amount of time. When it is done, the server can
continue normal operations, while the actual file backup proceeds.

%prep

%setup

%install
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;
make DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} mandir=%{_mandir} install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-, root, root)
%config(noreplace,missingok) %attr(600, root, root) %{_sysconfdir}/mylvmbackup.conf
%config(noreplace) %{_datadir}/%{name}/*.pm
%doc ChangeLog COPYING CREDITS INSTALL README TODO
%doc %{_mandir}/man1/%{name}.1*
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
