Name:           perl-SGMLSpm
Version:        1.03ii
Release:        21%{?dist}
Summary:        Perl library for parsing the output of nsgmls

Group:          Development/Libraries
License:        GPLv2+
URL:            http://search.cpan.org/dist/SGMLSpm/
Source0:        http://www.cpan.org/authors/id/D/DM/DMEGG/SGMLSpm-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       openjade

%description
Perl programs can use the SGMLSpm module to help convert SGML, HTML or XML
documents into new formats.


%prep
%setup -q -n SGMLSpm

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT{%{_bindir},%{perl_vendorlib}}
make install_system \
    BINDIR=$RPM_BUILD_ROOT%{_bindir} \
    PERL5DIR=$RPM_BUILD_ROOT%{perl_vendorlib}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README COPYING
%{_bindir}/sgmlspl
%{perl_vendorlib}/SGMLS*
%{perl_vendorlib}/skel.pl


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.03ii-21
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03ii-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03ii-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.03ii-18
- Rebuild for perl 5.10 (again)

* Fri Jan 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.03ii-17
- rebuild for new perl

* Thu Oct 26 2007 Ondrej Vasik <ovasik@redhat.com> - 1.03ii-16.4
- added base documentation
- fixed indents

* Mon Oct 22 2007 Ondrej Vasik <ovasik@redhat.com> - 1.03ii-16.3
- added dist tag
- License to GPL+
- spec file cleanup (all things from merge review by pnemade #226278)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.03ii-16.2.1
- rebuild

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 1.03ii-16.2
- rebuild for new perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Sat Apr 30 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.03ii-15
- Specfile cleanup. (#156483)

* Wed Sep 22 2004 Than Ngo <than@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 28 2003 Tim Waugh <twaugh@redhat.com> 1.03ii-12
- Use vendorlib not sitelib (bug #73493).
- Own %%{perldir}/SGMLS (bug #73922).

* Tue Jan 28 2003 Tim Waugh <twaugh@redhat.com> 1.03ii-11
- Rebuilt.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Sat Dec 14 2002 Tim Powers <timp@redhat.com> 
- don't use rpms internal dep generator

* Mon Nov 25 2002 Tim Waugh <twaugh@redhat.com> 1.03ii-9
- Fix URL (bug #71895).

* Mon Nov 25 2002 Tim Waugh <twaugh@redhat.com> 1.03ii-8
- Rebuild to get automatic provides: right.

* Wed Nov 20 2002 Tim Powers <timp@redhat.com> 1.03ii-7
- rebuild in current collinst

* Mon Jun 17 2002 Tim Waugh <twaugh@redhat.com> 1.03ii-6
- Rebuild in new environment.

* Sun Jan 14 2001 Tim Waugh <twaugh@redhat.com> 1.03ii-5
- Add defattr to files section.

* Mon Jan 08 2001 Tim Waugh <twaugh@redhat.com>
- Change group.
- rm before install.
- Change Copyright: to License:.
- Remove Packager: line.

* Mon Jan 08 2001 Tim Waugh <twaugh@redhat.com>
- Based on Eric Bischoff's new-trials packages.
