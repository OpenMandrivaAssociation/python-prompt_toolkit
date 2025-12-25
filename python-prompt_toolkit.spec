%global pypi_name prompt_toolkit

Name:           python-%{pypi_name}
Version:	3.0.52
Release:	1
Summary:        Library for building powerful interactive command lines in Python
Group:		Development/Python
License:        BSD
URL:            https://github.com/jonathanslenders/python-prompt-toolkit
Source0: https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)

Obsoletes:	python2-%{pypi_name} < %{EVRD}

%description
prompt_toolkit is a library for building powerful interactive command lines
and terminal applications in Python.

%files
%doc README.rst AUTHORS.rst CHANGELOG
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py*.*.egg-info
