Name:       c-515-10
Version:    1.0
Release:    1%{?dist}
Summary:    Программа студента Ostromogilskiia группы B20-505
Group:      Testing
License:    GPL
URL:        https://github.com/NeOStromag/-OSS_LABS
Source:     %{name}-%{version}.tar.gz
BuildRequires: gcc

%global debug_package %{nil}

%description
A test package

%prep
%setup -q

%build
gcc -O2 -o c-515-10 c-515-10.c

%install
mkdir -p %{buildroot}%{_bindir}
cp c-515-10 %{buildroot}%{_bindir}
sudo rpm -i ~/rpmbuild/RPMS/noarch/515-10-1.0-1.fc37.noarch.rpm --force

%files
%{_bindir}/c-515-10

%changelog
* Thu Oct 16 2012 <Ostromogilskii>
- Added %{_bindir}/c-515-10
