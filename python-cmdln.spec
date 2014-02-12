%define rname cmdln
%define debug_package %{nil}

Summary:	An improved cmd.py for easily building good multi-command scripts
Name:		python-%{rname}
Version:	1.1.2
Release:	2
License:	MIT License
Group:		Development/Python
URL:		http://code.google.com/p/cmdln/
Source0:	http://cmdln.googlecode.com/files/%{rname}-%{version}.zip
BuildRequires:	python-setuptools

%description
cmdln.py is an extension of Python's default cmd.py module that provides "a 
simple framework for writing line-oriented command interpreters". The idea 
(with both cmd.py and cmdln.py) is to be able to quickly build
multi-sub-command tools (think cvs or svn) and/or simple interactive shells
(think gdb or pdb). cmdln.py's extensions make it more natural to write
sub-commands, integrate optparse for simple option processing, and make having
good command documentation easier.

%prep

%setup -q -n %{rname}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__python} setup.py install \
    --root="%{buildroot}" \
    --prefix="%{_prefix}" \
    --record=INSTALLED_FILES

%files
%doc LICENSE.txt README.txt docs/ examples/
%{py_puresitedir}/*
