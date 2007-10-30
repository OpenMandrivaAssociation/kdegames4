%define revision 730797

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%if %unstable
%define dont_strip 1
%endif

%define lib_major 1
%define lib_name_orig libkdegames4
%define lib_name %mklibname kdegames4 %{lib_major}

Name:		kdegames4
Summary:	KDE - Games
Version:        3.94.1
Release: 	%mkrel 0.%revision.1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPL
URL:		ftp://ftp.kde.org/pub/kde/stable/%version/src/
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdegames-%version.%revision.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdegames-%version.tar.bz2
%endif
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel
BuildRequires: libxml2-utils

Requires: kde4-katomic
Requires: kde4-kbackgammon
Requires: kde4-kbattleship
Requires: kde4-kblackbox
Requires: kde4-kbounce
Requires: kde4-klines
Requires: kde4-kmahjongg
Requires: kde4-kmines
Requires: kde4-kolf
Requires: kde4-konquest
Requires: kde4-kpat
Requires: kde4-kreversi
Requires: kde4-ksame
Requires: kde4-kshisen
Requires: kde4-kspaceduel
Requires: kde4-ktuberling
Requires: kde4-kwin4
Requires: kde4-lskat
Requires: kde4-ksudoku
Requires: kde4-kgoldrunner
Requires: kde4-ktuberling
Requires: kde4-kiriki
Requires: kde4-kjumpingcube
Requires: kde4-bovo
Requires: kde4-ksquares
Requires: kde4-knetwalk

%description
Games for the K Desktop Environment.
This is a compilation of various games for KDE project
	- katomic: build complex atoms with a minimal amount of moves
	- kbackgammon: play backgammon against a local human player, via a
               game server or against GNU Backgammon (not included)
	- kbattleship: battleship game with built-in game server
	- kblackbox: find atoms in a grid by shooting electrons
	- kbounce: claim areas and don't get disturbed
	- klines: place 5 equal pieces together, but wait, there are 3 new ones
	- mahjongg: a tile laying patience
	- kmines: the classical mine sweeper
	- kolf: a golf game
	- konquest: conquer the planets of your enemy
	- kpat: several patience card games
	- kreversi: the old reversi board game, also known as othello
	- ksame: collect pieces of the same color
	- kshisen: patience game where you take away all pieces
	- kspaceduel: two player game with shooting spaceships flying around a sun
	- ktuberling: kids game: make your own potato (NO french fries!)
	- kwin4: place 4 pieces in a row
	- Lskat: lieutnant skat
	- Ksudoku: Play, create and solve sudoku grids
	- KGoldrunner: a game of action and puzzle solving.
	- KTuberling: "potato editor" game
	- Kiriki: Close of Yahtzee
	- Kjumpingcube: a tactical game for number-crunchers
	- Bovo: classic pen and paper game
	- KSquares: an implementation of the popular paper based game squares
	- Knetwalk: Turn the board pieces to get all computers connected

%files
%defattr(-,root,root)

#--------------------------------------------------------------------

%package core
Summary:        Common files needed by Kdegames4 packages
Group:          Graphical desktop/KDE

%description core
Common files needed by Kdegames4 packages

%files core
%defattr(-,root,root)
%_kde_appsdir/kdegames/pics/star.png
%_kde_appsdir/carddecks
%_kde_iconsdir/oxygen/*/actions/lastmoves.*
%_kde_iconsdir/oxygen/*/actions/legalmoves.*
%_kde_datadir/config.kcfg/*

#--------------------------------------------------------------------

%package devel
Summary:	Headers files for kdegames
Group:		Development/KDE and Qt
Provides:   %lib_name_orig-devel = %epoch:%version-%release
Provides:   %lib_name-devel = %epoch:%version-%release
Requires:	kdelibs4-devel 
Obsoletes:  %lib_name-devel < 1:3.93.0-0.714146.1

%description devel
Headers files needed to build applications based on kdegames applications.

%files devel
%defattr(-,root,root,-)
%_kde_datadir/apps/cmake/modules/FindLibKDEGames.cmake
%_kde_datadir/apps/cmake/modules/GGZ.cmake
%_kde_libdir/*.so
%_kde_includedir/*

#-----------------------------------------------------------------------------

%package -n     kde4-kgoldrunner
Summary:        KGoldrunner, a game of action and puzzle solving
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kgoldrunner4

%description -n kde4-kgoldrunner

KGoldrunner, a game of action and puzzle solving. 
Run through the maze, dodge your enemies, collect 
all the gold and climb up to the next level.

%files -n kde4-kgoldrunner
%defattr(-,root,root)
%attr(0755,root,root) %_kde_bindir/kgoldrunner
%_kde_datadir/applications/kde4/KGoldrunner.desktop
%_kde_appsdir/kgoldrunner
%dir %_kde_docdir/HTML/en/kgoldrunner
%doc %_kde_docdir/HTML/en/kgoldrunner/index.cache.bz2
%doc %_kde_docdir/HTML/en/kgoldrunner/index.docbook
%doc %_kde_docdir/HTML/en/kgoldrunner/*.png
%_kde_iconsdir/hicolor/*/apps/kgoldrunner.png

#-----------------------------------------------------------------------------

%package -n     kde4-kbackgammon
Summary:        Backgammon Game
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kbackgammon4

%description -n kde4-kbackgammon
kbackgammon: play backgammon against a local human player, via a
               game server or against GNU Backgammon (not included)

%files -n kde4-kbackgammon
%defattr(-,root,root)
%_kde_bindir/kbackgammon
%_kde_datadir/applications/kde4/kbackgammon.desktop
%_kde_docdir/HTML/en/kbackgammon
%_kde_iconsdir/hicolor/*/apps/kbackgammon*
%_kde_appsdir/kbackgammon/kbackgammonui.rc
%_kde_appsdir/kbackgammon/pics/*
%dir %_kde_appsdir/kbackgammon/sounds
%_kde_appsdir/kbackgammon/sounds/*
%_kde_appsdir/kbackgammon/kbackgammon.notifyrc

#-----------------------------------------------------------------------------

%package -n     kde4-katomic
Summary:        Build complex atoms with a minimal amount of moves
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       katomic4

%description -n kde4-katomic
katomic: build complex atoms with a minimal amount of moves

%files -n kde4-katomic
%defattr(-,root,root)
%_kde_bindir/katomic
%_kde_datadir/applications/kde4/katomic.desktop
%doc %_kde_docdir/HTML/en/katomic/index.cache.bz2
%doc %_kde_docdir/HTML/en/katomic/index.docbook
%_kde_iconsdir/hicolor/*/apps/katomic.png
%_kde_appsdir/katomic/levels/*
%_kde_appsdir/katomic/pics/default_theme.svgz
%_kde_appsdir/katomic/katomicui.rc

#-----------------------------------------------------------------------------

%package -n     kde4-kblackbox
Summary:        Find atoms in a grid by shooting electrons
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kblackbox4

%description -n kde4-kblackbox
kblackbox: find atoms in a grid by shooting electrons

%files -n kde4-kblackbox
%defattr(-,root,root)
%_kde_bindir/kblackbox
%_kde_datadir/applications/kde4/kblackbox.desktop
%_kde_appsdir/kblackbox/kblackboxui.rc
%_kde_appsdir/kblackbox/pics/kblackbox.svgz
%dir %_kde_docdir/HTML/en/kblackbox
%doc %_kde_docdir/HTML/en/kblackbox/*
%_kde_iconsdir/hicolor/*/apps/kblackbox.png

#-----------------------------------------------------------------------------

%package -n     kde4-ktuberling
Summary:        KTuberling: "potato editor" game
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       ktuberling4

%description -n kde4-ktuberling

KTuberling is a "potato editor" game intended for small 
children and adults who remain young at heart. The game 
has no winner; the only purpose is to make the funniest 
faces you can.

%files -n kde4-ktuberling
%defattr(-,root,root)
%_kde_bindir/ktuberling
%_kde_datadir/applications/kde4/ktuberling.desktop
%_kde_appsdir/ktuberling
%_kde_docdir/HTML/en/ktuberling
%_kde_iconsdir/hicolor/*/apps/ktuberling.png

#-----------------------------------------------------------------------------

%package -n     kde4-kbounce
Summary:        Claim areas and don't get disturbed
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kbounce4

%description -n kde4-kbounce
kbounce: claim areas and don't get disturbed

%files -n kde4-kbounce
%defattr(-,root,root)
%_kde_bindir/kbounce
%_kde_datadir/applications/kde4/kbounce.desktop
%_kde_appsdir/kbounce/kbounceui.rc
%_kde_appsdir/kbounce/themes/*
%dir %_kde_datadir/apps/kbounce/sounds
%_kde_datadir/apps/kbounce/sounds/*.au
%doc %_kde_docdir/HTML/en/kbounce/index.cache.bz2
%doc %_kde_docdir/HTML/en/kbounce/index.docbook
%doc %_kde_docdir/HTML/en/kbounce/*.png

#-----------------------------------------------------------------------------

%package -n     kde4-kspaceduel
Summary:        Two player game with shooting spaceships flying around a sun
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kspaceduel4

%description -n kde4-kspaceduel
kspaceduel: two player game with shooting spaceships flying around a sun

%files -n kde4-kspaceduel
%defattr(-,root,root)
%_kde_bindir/kspaceduel
%_kde_datadir/applications/kde4/kspaceduel.desktop
%_kde_appsdir/kspaceduel
%doc %_kde_docdir/HTML/en/kspaceduel/index.cache.bz2
%doc %_kde_docdir/HTML/en/kspaceduel/index.docbook
%doc %_kde_docdir/HTML/en/kspaceduel/kspaceduel3.png
%_kde_iconsdir/hicolor/*/apps/kspaceduel.png

#-----------------------------------------------------------------------------

%package -n     kde4-kreversi
Summary:        Old reversi board game, also known as othello
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kreversi4

%description -n kde4-kreversi
kreversi: the old reversi board game, also known as othello

%files -n kde4-kreversi
%defattr(-,root,root)
%_kde_bindir/kreversi
%_kde_datadir/applications/kde4/kreversi.desktop
%_kde_appsdir/kreversi
%_kde_iconsdir/hicolor/*/apps/kreversi.png
%dir %_kde_docdir/HTML/en/kreversi
%doc %_kde_docdir/HTML/en/kreversi/index.cache.bz2
%doc %_kde_docdir/HTML/en/kreversi/index.docbook
%doc %_kde_docdir/HTML/en/kreversi/kreversi-configuration.png
%doc %_kde_docdir/HTML/en/kreversi/kreversi1.png

#-----------------------------------------------------------------------------

%package -n     kde4-kolf
Summary:        A golf game
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kolf4

%description -n kde4-kolf
kolf: a golf game

%files -n kde4-kolf
%defattr(-,root,root)
%_kde_bindir/kolf
%_kde_datadir/applications/kde4/kolf.desktop
%_kde_appsdir/kolf
%doc %_kde_docdir/HTML/en/kolf/index.cache.bz2
%doc %_kde_docdir/HTML/en/kolf/index.docbook
%_kde_datadir/icons/hicolor/*/apps/kolf.png

#-----------------------------------------------------------------------------

%package -n     kde4-konquest
Summary:        Conquer the planets of your enemy
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       konquest4

%description -n kde4-konquest
konquest: conquer the planets of your enemy

%files -n kde4-konquest
%defattr(-,root,root)
%_kde_bindir/konquest
%_kde_datadir/applications/kde4/konquest.desktop
%_kde_appsdir/konquest
%doc %_kde_docdir/HTML/en/konquest/index.cache.bz2
%doc %_kde_docdir/HTML/en/konquest/index.docbook
%_kde_datadir/icons/hicolor/*/apps/konquest.png


#-----------------------------------------------------------------------------

%package -n     kde4-ksame
Summary:        Collect pieces of the same color
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       ksame4

%description -n kde4-ksame
ksame: collect pieces of the same color

%files -n kde4-ksame
%defattr(-,root,root)
%_kde_bindir/ksame
%_kde_appsdir/ksame/ksameui.rc
%_kde_datadir/applications/kde4/ksame.desktop
%_kde_appsdir/ksame/pics/default_theme.svgz
%dir %_kde_docdir/HTML/en/ksame
%doc %_kde_docdir/HTML/en/ksame/index.cache.bz2
%doc %_kde_docdir/HTML/en/ksame/index.docbook
%_kde_datadir/icons/hicolor/*/apps/ksame.png

#-----------------------------------------------------------------------------

%package -n     kde4-kmahjongg
Summary:        A tile laying patience
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kmahjongg4

%description -n kde4-kmahjongg
Kmahjongg: a tile laying patience

%files -n kde4-kmahjongg
%defattr(-,root,root)
%_kde_bindir/kmahjongg
%_kde_datadir/applications/kde4/kmahjongg.desktop
%_kde_appsdir/kmahjongg/kmahjonggui.rc
%_kde_appsdir/kmahjongg/layouts/*
%_kde_appsdir/kmahjongglib/backgrounds/*
%_kde_appsdir/kmahjongglib/tilesets/*
%dir %_kde_docdir/HTML/en/kmahjongg
%doc %_kde_docdir/HTML/en/kmahjongg/index.cache.bz2
%doc %_kde_docdir/HTML/en/kmahjongg/index.docbook
%doc %_kde_docdir/HTML/en/kmahjongg/*.png
%_kde_datadir/icons/hicolor/*/apps/kmahjongg.png

#-----------------------------------------------------------------------------

%package -n     kde4-kbattleship
Summary:        Battleship game with built-in game server
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kbattleship4

%description -n kde4-kbattleship
kbattleship: battleship game with built-in game server

%files -n kde4-kbattleship
%defattr(-,root,root)
%_kde_bindir/kbattleship
%_kde_datadir/applications/kde4/kbattleship.desktop
%doc %_kde_docdir/HTML/en/kbattleship/index.cache.bz2
%doc %_kde_docdir/HTML/en/kbattleship/index.docbook
%_kde_iconsdir/hicolor/*/apps/kbattleship.png
%_kde_appsdir/kbattleship/kbattleshipui.rc
%_kde_appsdir/kbattleship/pictures/default_theme.svgz
%_kde_appsdir/kbattleship/sounds/*

#-----------------------------------------------------------------------------

%package -n     kde4-kiriki
Summary:        Kiriki: Close of Yahtzee 
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kiriki4

%description -n kde4-kiriki

Kiriki is a dice game, written for KDE 4. 
It is a clone of Gnome Tali (gtali) that is a clone of Yahtzee!

%files -n kde4-kiriki
%defattr(-,root,root)
%_kde_bindir/kiriki
%_kde_datadir/applications/kde4/kiriki.desktop
%doc %_kde_docdir/HTML/en/kiriki/index.cache.bz2
%doc %_kde_docdir/HTML/en/kiriki/index.docbook
%_kde_iconsdir/hicolor/*/apps/kiriki.png
%_kde_appsdir/kiriki/images/*
%_kde_appsdir/kiriki/kirikiui.rc

#-----------------------------------------------------------------------------

%package -n     kde4-ksudoku
Summary:        KSudoku - Play, create and solve sudoku grids 
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       ksudoku4

%description -n kde4-ksudoku

The word Sudoku means "single number in an alloted place" in Japanese. These
are the basic rules. Every sudoku Sudoku is a square of 81 cells divided into
9 columns and 9 rows and in 9 subsquares (3x3) of 9 cells each. Solving takes
usually from 10 to 30 minutes, depending on puzzle level, your skill and
experience.

Some cells are filled with a number at the beginnning: the remaining are to
be filled by the player using numbers from 1 to 9, without repeating a number
twice on each column, row or subsuquare (each of them must contain only
one 1, one 2, one 3, and so on). The game requires logic and patience.
The numerals in Sudoku puzzles are used for convenience (for example in 16x16
board we use letters): arithmetic relationships between numbers are irrelevant.

This program supports also 16x16 games with numbers from 1 to 16 and 256
cells with 16 cols, rows and subsquares! (if normal sudoku are not enough for
you).

More information at http://en.wikipedia.org/wiki/Sudoku

%files -n kde4-ksudoku
%defattr(-,root,root)
%_kde_bindir/ksudoku
%_kde_datadir/applications/kde4/ksudoku.desktop
%_kde_appsdir/ksudoku/4x4.desktop
%_kde_appsdir/ksudoku/4x4.xml
%_kde_appsdir/ksudoku/Jigsaw.desktop
%_kde_appsdir/ksudoku/Jigsaw.xml
%_kde_appsdir/ksudoku/Samurai.desktop
%_kde_appsdir/ksudoku/Samurai.xml
%_kde_appsdir/ksudoku/XSudoku.desktop
%_kde_appsdir/ksudoku/XSudoku.xml
%_kde_appsdir/ksudoku/ksudokuui.rc
%_kde_appsdir/ksudoku/TinySamurai.desktop
%_kde_appsdir/ksudoku/TinySamurai.xml
%_kde_appsdir/ksudoku/icons
%_kde_datadir/config/ksudokurc
%_kde_iconsdir/hicolor/*/apps/ksudoku.png

%dir %_kde_docdir/HTML/en/ksudoku
%doc %_kde_docdir/HTML/en/ksudoku/index.cache.bz2
%doc %_kde_docdir/HTML/en/ksudoku/index.docbook

#-----------------------------------------------------------------------------

%package -n     kde4-bovo
Summary:        Bovo: classic pen and paper game
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       bovo4

%description -n kde4-bovo

Bovo is a KDE 4 game, modeled upon a classic pen and paper game, 
where you try to connect five in a row prior to your opponent.

%files -n kde4-bovo
%defattr(-,root,root)
%_kde_bindir/bovo
%_kde_datadir/applications/kde4/bovo.desktop
%_kde_appsdir/bovo/bovoui.rc
%_kde_appsdir/bovo/themes/gomoku/theme.svg
%_kde_appsdir/bovo/themes/gomoku/themerc
%_kde_appsdir/bovo/themes/highcontrast/theme.svg
%_kde_appsdir/bovo/themes/highcontrast/themerc
%_kde_appsdir/bovo/themes/scribble/theme.svg
%_kde_appsdir/bovo/themes/scribble/themerc
%_kde_appsdir/bovo/themes/spacy/theme.svg
%_kde_appsdir/bovo/themes/spacy/themerc
%doc %_kde_docdir/HTML/en/bovo/index.cache.bz2
%doc %_kde_docdir/HTML/en/bovo/index.docbook

#-----------------------------------------------------------------------------

%package -n     kde4-kjumpingcube
Summary:        kjumpingcube: a tactical game for number-crunchers
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kjumpingcube4

%description -n kde4-kjumpingcube

KJumpingCube is a tactical one or two-player game. The playing field 
consists of squares that contains points which can be increased. By 
this you can gain more fields and finally win the board over.

%files -n kde4-kjumpingcube
%defattr(-,root,root)
%_kde_bindir/kjumpingcube
%_kde_datadir/applications/kde4/kjumpingcube.desktop
%_kde_appsdir/kjumpingcube/kjumpingcubeui.rc
%_kde_appsdir/kjumpingcube/pics/default.desktop
%_kde_appsdir/kjumpingcube/pics/default.svg
%doc %_kde_docdir/HTML/en/kjumpingcube/index.cache.bz2
%doc %_kde_docdir/HTML/en/kjumpingcube/index.docbook
%_kde_iconsdir/hicolor/*/apps/kjumpingcube.png

#-----------------------------------------------------------------------------

%package -n     kde4-klines
Summary:        Place 5 equal pieces together, but wait, there are 3 new ones
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       klines4

%description -n kde4-klines
klines: place 5 equal pieces together, but wait, there are 3 new ones

%files -n kde4-klines
%defattr(-,root,root)
%_kde_bindir/klines
%_kde_datadir/applications/kde4/klines.desktop
%_kde_appsdir/klines
%_kde_docdir/HTML/en/klines
%_kde_iconsdir/hicolor/*/apps/klines.png

#-----------------------------------------------------------------------------

%package -n     kde4-kmines
Summary:        The classical mine sweeper
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kmines4

%description -n kde4-kmines
kmines: the classical mine sweeper

%files -n kde4-kmines
%defattr(-,root,root)
%_kde_bindir/kmines
%_kde_datadir/applications/kde4/kmines.desktop
%_kde_appsdir/kmines
%_kde_datadir/config/kmines.knsrc
%doc %_kde_docdir/HTML/en/kmines/index.cache.bz2
%doc %_kde_docdir/HTML/en/kmines/index.docbook
%doc %_kde_docdir/HTML/en/kmines/kmines1.png
%doc %_kde_docdir/HTML/en/kmines/kmines2.png
%_kde_iconsdir/hicolor/*/apps/kmines.png

#-----------------------------------------------------------------------------

%package -n     kde4-knetwalk
Summary:        Turn the board pieces to get all computers connected. 
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       knetwalk4

%description -n kde4-knetwalk

Turn the board pieces to get all computers connected.

%files -n kde4-knetwalk
%defattr(-,root,root)
%_kde_bindir/knetwalk
%_kde_datadir/applications/kde4/knetwalk.desktop
%_kde_appsdir/knetwalk/knetwalk.notifyrc
%_kde_appsdir/knetwalk/knetwalkui.rc
%_kde_appsdir/knetwalk/sounds/click.wav
%_kde_appsdir/knetwalk/sounds/connect.wav
%_kde_appsdir/knetwalk/sounds/start.wav
%_kde_appsdir/knetwalk/sounds/turn.wav
%_kde_appsdir/knetwalk/sounds/win.wav
%_kde_appsdir/knetwalk/themes/default.desktop
%_kde_appsdir/knetwalk/themes/default.svgz
%_kde_iconsdir/hicolor/*/apps/knetwalk.*

%dir %_kde_docdir/HTML/en/knetwalk
%doc %_kde_docdir/HTML/en/knetwalk/index.cache.bz2
%doc %_kde_docdir/HTML/en/knetwalk/index.docbook

#-----------------------------------------------------------------------------

%package -n     kde4-kpat
Summary:        Several patience card games
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kpat4

%description -n kde4-kpat
kpat: several patience card games

%files -n kde4-kpat
%defattr(-,root,root)
%_kde_bindir/kpat
%_kde_datadir/applications/kde4/kpat.desktop
%_kde_appsdir/kpat/backgrounds/background.svg
%_kde_appsdir/kpat/kpatui.rc
%_kde_appsdir/kpat/pile.svg
%_kde_appsdir/kpat/won.svg
%doc %_kde_docdir/HTML/en/kpat
%_kde_iconsdir/hicolor/*/apps/kpat.png

#-----------------------------------------------------------------------------

%package -n     kde4-kshisen
Summary:        Patience game where you take away all pieces
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kshisen4

%description -n kde4-kshisen
Kshisen: patience game where you take away all pieces

%files -n kde4-kshisen
%defattr(-,root,root)
%_kde_bindir/kshisen
%_kde_datadir/applications/kde4/kshisen.desktop
%_kde_appsdir/kshisen/kshisenui.rc
%doc %_kde_docdir/HTML/en/kshisen/index.cache.bz2
%doc %_kde_docdir/HTML/en/kshisen/index.docbook
%doc %_kde_docdir/HTML/en/kshisen/kshisen-configuration.png
%doc %_kde_docdir/HTML/en/kshisen/score-formula.png
%_kde_iconsdir/hicolor/*/apps/kshisen.png

#-----------------------------------------------------------------------------

%package -n     kde4-ksquares
Summary:        KSquares: an implementation of the popular paper based game squares
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       ksquares4

%description -n kde4-ksquares
KSquares is an implementation of the popular paper based game squares. 
You must draw lines to complete squares, the player with the most s
quares wins.

%files -n kde4-ksquares
%defattr(-,root,root)
%_kde_bindir/ksquares
%_kde_datadir/applications/kde4/ksquares.desktop
%_kde_appsdir/ksquares/ksquaresui.rc
%dir %_kde_docdir/HTML/en/ksquares
%doc %_kde_docdir/HTML/en/ksquares/index.cache.bz2
%doc %_kde_docdir/HTML/en/ksquares/index.docbook
%_kde_iconsdir/hicolor/*/apps/ksquares.png
%_kde_iconsdir/hicolor/scalable/actions/ksquares_ai.svgz
%_kde_iconsdir/hicolor/scalable/actions/ksquares_display.svgz

#-----------------------------------------------------------------------------

%package -n     kde4-kwin4
Summary:        Place 4 pieces in a row
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kwin44

%description -n kde4-kwin4
kwin4: place 4 pieces in a row

%files -n kde4-kwin4
%defattr(-,root,root)
%_kde_bindir/kwin4
%_kde_bindir/kwin4proc
%_kde_datadir/applications/kde4/kwin4.desktop
%_kde_appsdir/kwin4
%_kde_docdir/HTML/en/kwin4
%_kde_iconsdir/hicolor/*/apps/kwin4.png

#-----------------------------------------------------------------------------

%package -n     kde4-lskat
Summary:        Lieutnant skat
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       lskat4

%description -n kde4-lskat
lskat: lieutnant skat

%files -n kde4-lskat
%defattr(-,root,root)
%_kde_bindir/lskat
%_kde_datadir/applications/kde4/lskat.desktop
%_kde_appsdir/lskat
%dir %_kde_docdir/HTML/en/lskat
%doc %_kde_docdir/HTML/en/lskat/*
%_kde_iconsdir/hicolor/*/apps/lskat.png

#-----------------------------------------------------------------------------

%define libkdegames %mklibname kdegames 4

%package -n %libkdegames
Summary:    KDE 4 library
Group:      System/Libraries
Conflicts:  %{_lib}kdegames4 < 3.91
Obsoletes:  %{_lib}kdegames5 < 1:3.93.0-0.714146.1

%description -n %libkdegames
KDE 4 library.

%post -n %libkdegames -p /sbin/ldconfig
%postun -n %libkdegames -p /sbin/ldconfig

%files -n %libkdegames
%defattr(-,root,root)
%_kde_libdir/libkdegames.so.*

#-----------------------------------------------------------------------------

%define libkmahjongglib %mklibname kmahjongglib 4

%package -n %libkmahjongglib
Summary: KDE 4 library
Group: System/Libraries
Conflicts:  %{_lib}kdegames4 < 3.91
Obsoletes:  %{_lib}kmahjongglib5 < 1:3.93.0-0.714146.1

%description -n %libkmahjongglib
KDE 4 library.

%post -n %libkmahjongglib -p /sbin/ldconfig
%postun -n %libkmahjongglib -p /sbin/ldconfig

%files -n %libkmahjongglib
%defattr(-,root,root)
%_kde_libdir/libkmahjongglib.so.*

#-----------------------------------------------------------------------------

%define libkolflib %mklibname kolflib 1

%package -n %libkolflib
Summary: KDE 4 library
Group: System/Libraries
Conflicts:  %{_lib}kdegames4 < 3.91
Obsoletes: %{_lib}kolflib1.2.0 < 1:3.93.0-0.714146.1

%description -n %libkolflib
KDE 4 library.

%post -n %libkolflib -p /sbin/ldconfig
%postun -n %libkolflib -p /sbin/ldconfig

%files -n %libkolflib
%defattr(-,root,root)
%_kde_libdir/libkolflib.so.*

#-----------------------------------------------------------------------------

%define libkggzgames %mklibname kggzgames 4

%package -n %libkggzgames
Summary: KDE 4 library
Group: System/Libraries
Conflicts:  %{_lib}kdegames4 < 3.91

%description -n %libkggzgames
KDE 4 library.

%post -n %libkggzgames -p /sbin/ldconfig
%postun -n %libkggzgames -p /sbin/ldconfig

%files -n %libkggzgames
%defattr(-,root,root)
%_kde_libdir/libkggzgames.so.*

#-----------------------------------------------------------------------------

%define libkggzmod %mklibname kggzmod 4

%package -n %libkggzmod
Summary: KDE 4 library
Group: System/Libraries
Conflicts:  %{_lib}kdegames4 < 3.91

%description -n %libkggzmod
KDE 4 library.

%post -n %libkggzmod -p /sbin/ldconfig
%postun -n %libkggzmod -p /sbin/ldconfig

%files -n %libkggzmod
%defattr(-,root,root)
%_kde_libdir/libkggzmod.so.*

#-----------------------------------------------------------------------------

%define libkggznet %mklibname kggznet 4

%package -n %libkggznet
Summary: KDE 4 library
Group: System/Libraries
Conflicts:  %{_lib}kdegames4 < 3.91

%description -n %libkggznet
KDE 4 library.

%post -n %libkggznet -p /sbin/ldconfig
%postun -n %libkggznet -p /sbin/ldconfig

%files -n %libkggznet
%defattr(-,root,root)
%_kde_libdir/libkggznet.so.*

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdegames-%version

%build
%cmake_kde4 

%make

%install
rm -fr %buildroot

cd build

make install DESTDIR=%buildroot 

%clean
rm -fr %buildroot

