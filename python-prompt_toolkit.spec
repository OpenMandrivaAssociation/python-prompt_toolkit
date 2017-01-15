%global pypi_name prompt_toolkit

Name:           python-%{pypi_name}
Version:        1.0.9
Release:        1
Summary:        Library for building powerful interactive command lines in Python
Group:		Development/Java
License:        BSD
URL:            https://github.com/jonathanslenders/python-prompt-toolkit
Source0:        https://pypi.io/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-setuptools

%description
prompt_toolkit is a library for building powerful interactive command lines
and terminal applications in Python.

%package -n     python2-%{pypi_name}
Summary:        Library for building powerful interactive command lines in Python
%{?python_provide:%python_provide python2-%{pypi_name}}
%{?el6:Provides: python-%{pypi_name}}
 
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description -n python2-%{pypi_name}
prompt_toolkit is a library for building powerful interactive command lines
and terminal applications in Python.

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

cp -a . %py2dir

%build
python setup.py build
pushd %py2dir
python2 setup.py build

%install
python setup.py install --root=%buildroot
pushd %py2dir
python2 setup.py install --root=%buildroot



%files -n python2-%{pypi_name} 
%doc README.rst AUTHORS.rst CHANGELOG
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files
%doc README.rst AUTHORS.rst CHANGELOG
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.9-2
- Rebuild for Python 3.6

* Sun Dec 11 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.0.9-1
- Update to 1.0.9

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Tue Mar 29 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.60-1
- Update to 0.60

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.57-2
- Make the EL6 package provide python-prompt_toolkit too

* Sat Jan 09 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.57-1
- New upstream update

* Wed Jan 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.54-2
- Fix quiet setup
- Fix license
- Add AUTHORS.rst, CHANGELOG & TODO.rst

* Tue Dec 29 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.54-1
- Initial package.
