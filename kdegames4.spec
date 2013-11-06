Summary:	KDE - Games
Name:		kdegames4
Version:	4.11.3
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://games.kde.org/
Suggests:	bomber
Suggests:	bovo
Suggests:	granatier
Suggests:	kajongg
Suggests:	kapman
Suggests:	katomic
Suggests:	kblackbox
Suggests:	kblocks
Suggests:	kbounce
Suggests:	kbreakout
Suggests:	kdiamond
Suggests:	kfourinline
Suggests:	kgoldrunner
Suggests:	kigo
Suggests:	killbots
Suggests:	kiriki
Suggests:	kjumpingcube
Suggests:	klickety
Suggests:	klines
Suggests:	kmahjongg
Suggests:	kmines
Suggests:	knavalbattle
Suggests:	knetwalk
Suggests:	kolf
Suggests:	kollision
Suggests:	konquest
Suggests:	kpat
Suggests:	kreversi
Suggests:	kshisen
Suggests:	ksirk
Suggests:	ksnakeduel
Suggests:	kspaceduel
Suggests:	ksquares
Suggests:	ksudoku
Suggests:	ktuberling
Suggests:	kubrick
Suggests:	lskat
Suggests:	palapeli
Suggests:	picmi
BuildArch:	noarch

%description
Games for the K Desktop Environment.
This is a compilation of various games for KDE project:
- bomber: Arcade bombing game
- bovo: Classic pen and paper game
- granatier: KDE Bomberman game
- kajongg: Majongg game for KDE
- kapman: A Pac-Man clone
- katomic: Build complex atoms with a minimal amount of moves
- kblackbox: Find atoms in a grid by shooting electrons
- kblocks: Single player falling blocks puzzle game
- kbounce: Claim areas and don't get disturbed
- kbreakout: Breakout like game
- kdiamond: Three-in-a-row game
- kfourinline: Place 4 pieces in a row
- kgoldrunner: A game of action and puzzle solving
- kigo: Go board game for KDE
- killbots: KDE port of the classic BSD console game robots
- kiriki: Close of Yahtzee
- kjumpingcube: A tactical game for number-crunchers
- klickety: An adaptation of the Clickomania game
- klines: Place 5 equal pieces together, but wait, there are 3 new ones
- kmahjongg: A tile laying patience
- kmines: The classic mine sweeper
- knavalbattle: Battleship game with built-in game server
- knetwalk: Turn the board pieces to get all computers connected
- kolf: A golf game
- kollision: A simple ball dodging game
- konquest: Conquer the planets of your enemy
- kpat: Several patience card games
- kreversi: Old reversi board game, also known as othello
- kshisen: Patience game where you take away all pieces
- ksirk: Computerized version of a well known strategy board game
- ksnakeduel: Snake race played against the computer
- kspaceduel: Two player game with shooting spaceships flying around a sun
- ksquares: An implementation of the popular paper based game squares
- ksudoku: Play, create and solve sudoku grids
- ktuberling: "Potato editor" game
- kubrick: Game based on Rubik's Cube
- lskat: Lieutnant skat
- palapeli: Jigsaw puzzle game
- picmi: A nonogram logic game for KDE

%files

#-----------------------------------------------------------------------------

%prep
# Nothing

%build
# Nothing

%install
# Nothing

%changelog
* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Mon Feb 18 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Just a metapackage with Suggests from now on

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2
- Build without l10n-ru patch for now

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Mon Aug 06 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0
- Update files

* Mon Jul 16 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97
- Make better usage of KDE4 path macros
- Add control over library majors
- Convert BuildRequires to pkgconfig style
- Add pkgconfig(sndfile) to BuildRequires
- Re-diff and enable l10n-ru patch

* Thu Jun 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- Update to 4.8.95

* Tue Jun 26 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.90-1
- Update to 4.8.90
- Drop no longer needed Conflicts and Obsoletes
- Minor cleanups
- Disable patch (needs re-diff)

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.80-69.1mib2010.2
- New version 4.8.80 (aka 4.9 beta1), we use it because many KDE4 4.8.x games
  don't work well with phonon-gstreamer 4.6
- New libkdegames major (5->6)
- Drop all ggz related stuff
- Add libkdegamesprivate subpackage and library
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.0-69.1mib2010.2
+ Revision: 762514
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762514
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758099
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 750412
- New version

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-2
+ Revision: 744329
- Disable buggy rpm5 *feature*
- Fix file list
- Fix file list
- Fix BR
- New upstream tarball
- New upstream tarball 4.7.80
- New version 4.7.41
- Remove branch switch

* Mon Jun 13 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.4-1
+ Revision: 684404
- New version 4.6.4

* Fri May 13 2011 Funda Wang <fwang@mandriva.org> 1:4.6.3-1
+ Revision: 674022
- new version 4.6.3

* Tue Apr 05 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.2-1
+ Revision: 650772
- Remove mkrel
- New version 4.6.2

* Mon Feb 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.1-1
+ Revision: 640726
- New version 4.6.1

* Wed Jan 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.0-1
+ Revision: 632964
- New version KDE 4.6 Final

* Thu Jan 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.95-1mdv2011.0
+ Revision: 629120
- New version KDE 4.6 RC2

* Thu Dec 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.90-1mdv2011.0
+ Revision: 624062
- New upstream tarball

* Wed Dec 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.85-1mdv2011.0
+ Revision: 616343
- New upstream tarball

* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 1:4.5.80-1mdv2011.0
+ Revision: 601635
- new version 4.5.80 (aka 4.6 beta1)

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 1:4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599252
- update file list
- new snapshot 4.5.77

* Tue Nov 02 2010 Funda Wang <fwang@mandriva.org> 1:4.5.74-0.svn1192115.1mdv2011.0
+ Revision: 591858
- add sqlite3 as BR for kajongg
- more requires
- add more requires
- new snapshot 4.5.74

* Mon Oct 18 2010 Funda Wang <fwang@mandriva.org> 1:4.5.71-0.svn1184269.3mdv2011.0
+ Revision: 586556
- the correct place for kcardgame is kpat sub package

* Mon Oct 18 2010 Funda Wang <fwang@mandriva.org> 1:4.5.71-0.svn1184269.2mdv2011.0
+ Revision: 586555
- libkcardgame.so is not a devel file

* Wed Oct 13 2010 Funda Wang <fwang@mandriva.org> 1:4.5.71-0.svn1184269.1mdv2011.0
+ Revision: 585259
- update file list
- new snapshot

* Thu Sep 16 2010 Funda Wang <fwang@mandriva.org> 1:4.5.68-1mdv2011.0
+ Revision: 578800
- new snapshot 4.5.68

* Tue Sep 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.67-1mdv2011.0
+ Revision: 576503
- Fix file list
- New version 4.5.67

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.0-1mdv2011.0
+ Revision: 566568
- New upstream tarball
- Update to version 4.5.0

* Thu Jul 29 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.95-1mdv2011.0
+ Revision: 562877
- Fix file list
- Add buildrequires
- KDE 4.5 RC3

* Thu Jul 15 2010 Anssi Hannula <anssi@mandriva.org> 1:4.4.3-3mdv2011.0
+ Revision: 553774
- fix conflicts in bovo package

* Wed May 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-2mdv2010.1
+ Revision: 546159
- Rebuild in release mode

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-1mdv2010.1
+ Revision: 542101
- Update to version 4.4.3
- Fix devel package file list

* Wed Mar 31 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.2-1mdv2010.1
+ Revision: 530115
- Fix file list
- Update to version 4.4.2

* Tue Mar 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-1mdv2010.1
+ Revision: 513408
- Update to version 4.4.1

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-1mdv2010.1
+ Revision: 502610
- Update to version 4.4.0

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.98-1mdv2010.1
+ Revision: 498943
- Update to version 4.3.98 aka "kde 4.4 RC3"
- Update to version 4.3.98 aka "kde 4.4 RC3"

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.95-1mdv2010.1
+ Revision: 495992
- Update to version 4.3.95 aka "kde 4.4 RC2"
- Update to version 4.3.95 aka "kde 4.4 RC2"
- Remove the cp trick as the icons belong to an other package
- Add missing icons in hicolor

* Sun Jan 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.90-1mdv2010.1
+ Revision: 488618
- Fix file list
- Fix file list
- Update to kde 4.4 rc1

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.85-1mdv2010.1
+ Revision: 480818
- Fix file list
- Update to kde 4.4 beta2
  Remove merged patches
  Remove old unneded Buildrequires
- Add Gnugo as Requires for Kigo

* Sat Dec 05 2009 Funda Wang <fwang@mandriva.org> 1:4.3.80-1mdv2010.1
+ Revision: 473680
- finally fix building
- add palapeli
- bump versioned requires

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix version in BuildRequires
    - Update to kde 4.4 beta1

* Sat Nov 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.77-1mdv2010.1
+ Revision: 470788
- Add branch switch
- Fix typo in suggests

  + Funda Wang <fwang@mandriva.org>
    - New version 4.3.77

* Fri Nov 20 2009 Funda Wang <fwang@mandriva.org> 1:4.3.75-1mdv2010.1
+ Revision: 467591
- New version 4.3.75

* Wed Nov 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-2mdv2010.1
+ Revision: 465070
- Rebuild against new qt

* Sun Nov 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-1mdv2010.1
+ Revision: 463213
- Update to kde 4.3.73

* Tue Oct 06 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.2-1mdv2010.0
+ Revision: 454660
- New upstream release 4.3.2.

* Mon Oct 05 2009 Funda Wang <fwang@mandriva.org> 1:4.3.1-4mdv2010.0
+ Revision: 453846
- BUMP rel
- singled out kmahjongglib as required by all mahjongg-like games.

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix typo

* Sun Sep 13 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-2mdv2010.0
+ Revision: 438584
- Obsolete kde3 packages

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.1-1mdv2010.0
+ Revision: 423217
- New upstream release 4.3.1.

* Fri Aug 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.0-2mdv2010.0
+ Revision: 418983
- Rebuild for missing package
- Change requires into suggests
  Fix Ksirk summary

* Tue Aug 04 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.0-1mdv2010.0
+ Revision: 409416
- New upstream release 4.3.0.
- Update to KDE 4.3 RC3

* Sat Jul 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.96-1mdv2010.0
+ Revision: 394895
- Update to Rc2

* Sat Jun 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.95-2mdv2010.0
+ Revision: 389795
- Fix conflicts

* Fri Jun 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.95-1mdv2010.0
+ Revision: 389391
- Update to kde 4.3Rc1

* Thu Jun 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.90-1mdv2010.0
+ Revision: 382854
- Remove merged patches
- Update to beta2

* Fri May 29 2009 Funda Wang <fwang@mandriva.org> 1:4.2.88-1mdv2010.0
+ Revision: 380796
- fix file list
- New version 4.2.88

* Fri May 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.87-1mdv2010.0
+ Revision: 378822
- Update to kde   4.2.87

* Sat May 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.85-1mdv2010.0
+ Revision: 373564
- Update to kde 4.2.85
- Update to kde 4.2.85

* Sun May 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.71-0.svn961800.1mdv2010.0
+ Revision: 371234
- Update to kde 4.2.71

* Sat May 02 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.70-0.svn954171.1mdv2010.0
+ Revision: 370697
- Update to kde 4.2.70
  Add Ktron and Kdesnake
  Fix file list

* Sun Apr 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-3mdv2009.1
+ Revision: 364187
- Add some upstream patches from branch
        - Patch100: Kubrik : missing opengl include
- Remove Old tarball
  Fix crash in Ksirk at server connect (BKO: 187235 QMO: 49132)

* Fri Mar 27 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.2-1mdv2009.1
+ Revision: 361727
- Update with 4.2.2 try#1 packages

* Sat Feb 28 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.1-1mdv2009.1
+ Revision: 346212
- KDE 4.2.1 try#1 upstream release

* Mon Feb 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.0-2mdv2009.1
+ Revision: 340881
- Rebuild against qt4.5
- Fix bomber description

* Wed Jan 28 2009 Funda Wang <fwang@mandriva.org> 1:4.2.0-1mdv2009.1
+ Revision: 334820
- New version 4.2.0

* Fri Jan 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.96-1mdv2009.1
+ Revision: 327304
- Fix file list

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.96

* Sun Dec 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.85-1mdv2009.1
+ Revision: 314060
- New version KDE 4.2 Beta2

* Thu Dec 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.82-1mdv2009.1
+ Revision: 313374
- Update to kde 4.1.82

* Mon Dec 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.81-2mdv2009.1
+ Revision: 308661
- Rebuild

* Sun Nov 30 2008 Funda Wang <fwang@mandriva.org> 1:4.1.81-1mdv2009.1
+ Revision: 308426
- New version 4.1.81
- drop ksudoku build condition

* Wed Nov 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.80-3mdv2009.1
+ Revision: 306997
- Versionnate Obsoletes

* Tue Nov 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.80-2mdv2009.1
+ Revision: 306582
- some more obsoletes
- Obsoletes kdegames

  + Funda Wang <fwang@mandriva.org>
    - requires new game

* Thu Nov 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.80-1mdv2009.1
+ Revision: 304864
- New subpackage Bomber

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.80

* Mon Nov 17 2008 Funda Wang <fwang@mandriva.org> 1:4.1.73-2mdv2009.1
+ Revision: 303889
- add patch fixing ksudoku build

* Sat Nov 15 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.73-1mdv2009.1
+ Revision: 303397
- Fix BuildRequires
- Update to kde 4.1.73
- Fix Requires on core package

* Sun Oct 26 2008 Funda Wang <fwang@mandriva.org> 1:4.1.71-1mdv2009.1
+ Revision: 297352
- install kapman.desktop into correct dir
- require two new games
- update file list
- New version 4.1.71

* Sun Oct 12 2008 Funda Wang <fwang@mandriva.org> 1:4.1.2-3mdv2009.1
+ Revision: 292759
- move devel package section so that all the libs are declared
- fix wrong .so suffix of libkdegames
- devel package should requires libpackages

* Thu Oct 02 2008 Frederic Crozat <fcrozat@mandriva.com> 1:4.1.2-2mdv2009.0
+ Revision: 290841
- Add conflicts to ease upgrade

* Thu Sep 25 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.2-1mdv2009.0
+ Revision: 288309
- KDE 4.1.2 arriving.

* Sun Aug 31 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.1-1mdv2009.0
+ Revision: 277839
- Upgrade to forthcoming 4.1.1 packages

  + Funda Wang <fwang@mandriva.org>
    - update url

* Fri Jul 25 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.0-1mdv2009.0
+ Revision: 247585
- Update with Release Candidate 1 - 4.1.0

* Thu Jul 10 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.98-1mdv2009.0
+ Revision: 233190
- Update with Release Candidate 1 - 4.0.98

* Mon Jul 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.85-1mdv2009.0
+ Revision: 232461
- New version kde 4.0.85

* Sun Jun 29 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.84-2mdv2009.0
+ Revision: 229949
- Underlinnk patch was included upstream
- Fix br
- Update with new snapshot tarballs 4.0.84

* Mon Jun 23 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.83-2mdv2009.0
+ Revision: 228415
- Enabled ggz back, wrongly removed based on bad freeciv packaging.
- Commented ksudoku for now, since underlinking issue is happening upstream
- Added reference for proper ggz packaging, should discuss later with mdv staff best method to package mosules stuff
- Update with new snapshot tarballs 4.0.83
- Update with new snapshot tarballs 4.0.82

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jun 03 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.81-1mdv2009.0
+ Revision: 214719
- Update with new snapshot tarballs 4.0.81

* Sat May 24 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.80-1mdv2009.0
+ Revision: 210783
- New upstream kde4 4.1 beta1

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Own %%{_kde_appsdir}/kmahjongglib
    - Own better the folders

* Mon May 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.74-4mdv2009.0
+ Revision: 209203
- Remove description about kbackgammon
  Obsolete old kde4-kbackgammon

* Fri May 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.74-3mdv2009.0
+ Revision: 208266
- Rebuild against new kdebase4
- Versionate BuildRequires

* Fri May 16 2008 Funda Wang <fwang@mandriva.org> 1:4.0.74-2mdv2009.0
+ Revision: 208038
- New version 4.0.74

* Fri May 09 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.73-2mdv2009.0
+ Revision: 204789
- Say hello to kbreakout and ksirk
  Remove ggz-lib buildrequires and add a comment about that

* Wed May 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.72-2mdv2009.0
+ Revision: 202770
- Fix BuildRequires
- Update to kde 4.0.72
- Add new subpackage +> KBlocks
  Fix file list
  Fix provides ( copy / paste suxx )
- Fix Requires
- New sub packages kubrick kollision and kdiamond
  Fix File list
- New snapshot 4.0.69

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 alpha 1

* Fri Mar 28 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.3-1mdv2008.1
+ Revision: 191003
- Update for last stable release 4.0.3

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-2mdv2008.1
+ Revision: 182263
- Rebuild against new qt4 changes

* Sat Mar 01 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.2-1mdv2008.1
+ Revision: 177437
- New upstream bugfix release 4.0.2

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description

* Tue Feb 12 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.1-1mdv2008.1
+ Revision: 165897
- Update for 4.0.1

* Wed Jan 09 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.0-1mdv2008.1
+ Revision: 147335
- Updated to latest 4.0.0 stable

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New snapshot
      Kwin4 is now called Kfourinline

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-0.746784.1mdv2008.1
+ Revision: 117087
- New snapshot
  Obsolete libkolflib on libkolfprivate packag

* Fri Nov 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.742894.1mdv2008.1
+ Revision: 114116
- New snapshot

* Fri Nov 23 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.740193.1mdv2008.1
+ Revision: 111553
- New snapshot
  Package kcfg files in there own  package ( Bug #35626)

* Sat Nov 17 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.0-0.737137.1mdv2008.1
+ Revision: 109648
- KDE4 RC1

* Sun Nov 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.95.2-0.734589.2mdv2008.1
+ Revision: 107542
- Fix Requires

* Sun Nov 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.95.2-0.734589.1mdv2008.1
+ Revision: 107536
- New snapshot
  kbackgammon is not on the package anymore

* Fri Nov 02 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.95.1-0.731582.1mdv2008.1
+ Revision: 104988
- New snapshot post Rc1

* Tue Oct 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.1-0.730797.1mdv2008.1
+ Revision: 103774
- Fix File list
- New snashot

* Thu Oct 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.1-0.729193.1mdv2008.1
+ Revision: 102157
- New snapshot

* Sat Oct 20 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.0-0.727095.1mdv2008.1
+ Revision: 100515
- Kde 4 Beta 3

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Fri Sep 21 2007 Tiago Salem <salem@mandriva.com.br> 1:3.93.0-0.714146.1mdv2008.0
+ Revision: 91944
- Changing Obsoletes tags and updating tarball to a newer revision.

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with revision 711178

* Tue Sep 04 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.93.0-0.707981.1mdv2008.0
+ Revision: 79000
- Update with revision 707981
- Update with revision 706624

* Thu Aug 30 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92.0-0.706247.1mdv2008.0
+ Revision: 75096
- Update with revision 706247

* Wed Aug 29 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92.0-0.705994.1mdv2008.0
+ Revision: 73335
- Update with revision 705994

* Mon Aug 06 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92.0-0.696866.1mdv2008.0
+ Revision: 59504
- UPdate to revision 696866
- Update to revision 693322

* Wed Jul 04 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.91-0.682394.2mdv2008.0
+ Revision: 48038
- New snapshot post monday BIC
- Fix main package and the -core one

* Sat Jun 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.91-0.681524.1mdv2008.0
+ Revision: 46068
- Fix File list
- Start to fix file list to satisfy new kde layout

* Thu May 10 2007 Laurent Montel <lmontel@mandriva.org> 1:3.90.1-0.20070502.1mdv2008.0
+ Revision: 25996
- new snapshot

* Fri May 04 2007 Laurent Montel <lmontel@mandriva.org> 1:3.80.3-0.20070502.3mdv2008.0
+ Revision: 22301
- new snapshot
- new snapshot


* Sun Mar 11 2007 Laurent Montel <lmontel@mandriva.com> 3.80.3-0.20070311.3mdv2007.1
+ Revision: 141383
- new snapshot
- Fix spec file
- new snapshot
- new snapshot
- 3.80.3
- new snapshot

* Tue Jan 23 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070123.2mdv2007.1
+ Revision: 112289
- new snapshot

* Thu Jan 18 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070117.2mdv2007.1
+ Revision: 110236
- Update

* Wed Jan 10 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070109.2mdv2007.1
+ Revision: 107028
- Increase version because bot rebuild is stupid
- Update snapshot

* Wed Jan 03 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070103.1mdv2007.1
+ Revision: 103686
- Fix spec file
- Update
- Byebye menu macro

* Thu Dec 28 2006 Laurent Montel <lmontel@mandriva.com> 1:3.80-3mdv2007.1
+ Revision: 102279
- Import kdegames4

* Fri Nov 03 2006 Laurent Montel <lmontel@mandriva.com> 3.5.5-3mdv2007.0
- First package

