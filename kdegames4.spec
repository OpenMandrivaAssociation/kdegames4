%define kde_snapshot svn1040395

Name: kdegames4
Summary: KDE - Games
Version: 4.3.73
Release: %mkrel 1
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://games.kde.org/
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdegames-%version%kde_snapshot.tar.bz2
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel >= 2:4.2.98
BuildRequires: kdelibs4-experimental-devel >= 2:4.2.98
BuildRequires: libxml2-utils
# Do not comment ggz. For now we're excluding /etc/ggz.modules, but freeciv package is wrong too.
# read this if you have some doubt http://svn.ggzgamingzone.org/trac.cgi/browser/trunk/docs/ggz-project/packagers
BuildRequires: ggz-client-libs-devel
BuildRequires: qca2-devel
Suggests:   katomic
Suggests:   kbattleship
Suggests:   kblackbox
Suggests:   kbounce
Suggests:   klines
Suggests:   kmahjongg
Suggests:   kmines
Suggests:   kolf
Suggests:   konquest
Suggests:   kpat
Suggests:   kreversi
Suggests:   ksame
Suggests:   kshisen
Suggests:   kspaceduel
Suggests:   ktuberling
Suggests:   kfourinline
Suggests:   lskat
Suggests:   ksudoku
Suggests:   kgoldrunner
Suggests:   ktuberling
Suggests:   kiriki
Suggests:   kjumpingcube
Suggests:   bovo
Suggests:   ksquares
Suggests:   knetwalk
Suggests:   kollision
Suggests:   kubrick
Suggests:   kdiamond
Suggests:   kblocks
Suggests:   ksirk
Suggests:   kbreakout 
Suggests:   kapman
Suggests:   killbots
Suggests:   bomber
Suggests:   ktron
Suggests:   kdesnake

Obsoletes:  kde4-kbackgammon < 1:4.0.74-4  

%if %mdkversion >= 201000
Obsoletes:   kdegames < 1:3.5.10-3
Obsoletes:   kdegames3 < 1:3.5.10-3
%endif

%description
Games for the K Desktop Environment.
This is a compilation of various games for KDE project
	- katomic: build complex atoms with a minimal amount of moves
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
	- kfourinline: place 4 pieces in a row
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
Requires:       kdebase4-runtime
Conflicts:      kshisen < 1:4.2.95-2

%description core
Common files needed by Kdegames4 packages

%files core
%defattr(-,root,root)
%_kde_appsdir/kdegames
%_kde_appsdir/carddecks
%_kde_iconsdir/oxygen/*/actions/lastmoves.*
%_kde_iconsdir/oxygen/*/actions/legalmoves.*

#-----------------------------------------------------------------------------

%package -n     kgoldrunner
Summary:        KGoldrunner, a game of action and puzzle solving
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kgoldrunner
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kgoldrunner4
Obsoletes:      kde4-kgoldrunner < 1:4.0.68
Provides:       kde4-kgoldrunner = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kgoldrunner
KGoldrunner, a game of action and puzzle solving. 
Run through the maze, dodge your enemies, collect 
all the gold and climb up to the next level.

%files -n kgoldrunner
%defattr(-,root,root)
%attr(0755,root,root) %_kde_bindir/kgoldrunner
%_kde_datadir/applications/kde4/KGoldrunner.desktop
%_kde_datadir/config/kgoldrunner.knsrc
%_kde_appsdir/kgoldrunner
%_kde_docdir/*/*/kgoldrunner
%_kde_iconsdir/hicolor/*/apps/kgoldrunner.png

#-----------------------------------------------------------------------------

%package -n     kapman
Summary:        A Pac-Man clone
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Provides:       kapman4
Provides:       kde4-kapman = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kapman
Kapman is a Pac-Man clone.

%files -n kapman
%defattr(-,root,root)
%_kde_bindir/kapman
%_kde_datadir/applications/kde4/kapman.desktop
%_kde_appsdir/kapman
%_kde_docdir/*/*/kapman
%_kde_iconsdir/hicolor/*/apps/kapman.*
%_kde_datadir/sounds/kapman

#-----------------------------------------------------------------------------

%package -n     katomic
Summary:        Build complex atoms with a minimal amount of moves
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=katomic
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       katomic4
Obsoletes:      kde4-katomic < 1:4.0.68
Provides:       kde4-katomic = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n katomic
katomic: build complex atoms with a minimal amount of moves

%files -n katomic
%defattr(-,root,root)
%_kde_bindir/katomic
%_kde_datadir/applications/kde4/katomic.desktop
%_kde_docdir/*/*/katomic
%_kde_iconsdir/hicolor/*/apps/katomic.png
%_kde_appsdir/katomic
%_kde_appsdir/kconf_update/katomic-levelset-upd.pl
%_kde_appsdir/kconf_update/katomic-levelset.upd

#-----------------------------------------------------------------------------

%package -n     kblackbox
Summary:        Find atoms in a grid by shooting electrons
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kblackbox
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kblackbox4
Obsoletes:      kde4-kblackbox < 1:4.0.68
Provides:       kde4-kblackbox = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kblackbox
kblackbox: find atoms in a grid by shooting electrons

%files -n kblackbox
%defattr(-,root,root)
%_kde_bindir/kblackbox
%_kde_datadir/applications/kde4/kblackbox.desktop
%_kde_appsdir/kblackbox
%_kde_docdir/*/*/kblackbox
%_kde_iconsdir/hicolor/*/apps/kblackbox.png

#-----------------------------------------------------------------------------

%package -n     ktuberling
Summary:        KTuberling: "potato editor" game
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=ktuberling
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       ktuberling4
Obsoletes:      kde4-ktuberling < 1:4.0.68
Provides:       kde4-ktuberling = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n ktuberling
KTuberling is a "potato editor" game intended for small 
children and adults who remain young at heart. The game 
has no winner; the only purpose is to make the funniest 
faces you can.

%files -n ktuberling
%defattr(-,root,root)
%_kde_bindir/ktuberling
%_kde_datadir/applications/kde4/ktuberling.desktop
%_kde_appsdir/ktuberling
%_kde_docdir/*/*/ktuberling
%_kde_iconsdir/hicolor/*/apps/ktuberling.png

#-----------------------------------------------------------------------------

%package -n     kbounce
Summary:        Claim areas and don't get disturbed
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kbounce
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kbounce4
Obsoletes:      kde4-kbounce < 1:4.0.68
Provides:       kde4-kbounce = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kbounce
kbounce: claim areas and don't get disturbed

%files -n kbounce
%defattr(-,root,root)
%_kde_bindir/kbounce
%_kde_datadir/applications/kde4/kbounce.desktop
%_kde_appsdir/kbounce
%_kde_iconsdir/*/*/apps/kbounce*
%_kde_docdir/*/*/kbounce

#-----------------------------------------------------------------------------

%package -n     killbots
Summary:        KDE port of the classic BSD console game robots
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Provides:       kapman4
Provides:       kde4-killbots = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n killbots
Killbots is a KDE port of the classic BSD console game robots.

%files -n killbots
%defattr(-,root,root)
%_kde_bindir/killbots
%_kde_datadir/applications/kde4/killbots.desktop
%_kde_appsdir/killbots
%_kde_datadir/config.kcfg/killbots.kcfg
%_kde_docdir/*/*/killbots
%_kde_iconsdir/hicolor/*/apps/killbots.*

#-----------------------------------------------------------------------------

%package -n     kspaceduel
Summary:        Two player game with shooting spaceships flying around a sun
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kspaceduel
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Conflicts:      kdegames4-core < 3.96.1-0.740193.1
Provides:       kspaceduel4
Obsoletes:      kde4-kspaceduel < 1:4.0.68
Provides:       kde4-kspaceduel = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kspaceduel
kspaceduel: two player game with shooting spaceships flying around a sun

%files -n kspaceduel
%defattr(-,root,root)
%_kde_bindir/kspaceduel
%_kde_datadir/applications/kde4/kspaceduel.desktop
%_kde_appsdir/kspaceduel
%_kde_docdir/*/*/kspaceduel
%_kde_iconsdir/hicolor/*/apps/kspaceduel.png
%_kde_datadir/config.kcfg/kspaceduel.kcfg

#-----------------------------------------------------------------------------

%package -n     kreversi
Summary:        Old reversi board game, also known as othello
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kreversi
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kreversi4
Obsoletes:      kde4-kreversi < 1:4.0.68
Provides:       kde4-kreversi = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kreversi
kreversi: the old reversi board game, also known as othello

%files -n kreversi
%defattr(-,root,root)
%_kde_bindir/kreversi
%_kde_datadir/applications/kde4/kreversi.desktop
%_kde_appsdir/kreversi
%_kde_iconsdir/hicolor/*/apps/kreversi.png
%_kde_docdir/*/*/kreversi

#-----------------------------------------------------------------------------

%package -n     kolf
Summary:        A golf game
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kolf
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kolf4
Obsoletes:      kde4-kolf < 1:4.0.68
Provides:       kde4-kolf = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kolf
Kolf is a miniature golf game with 2d top-down view. Courses are dynamic,
and up to 10 people can play at once in competition. Kolf comes equipped
with a variety of playgrounds and tutorial courses.

%files -n kolf
%defattr(-,root,root)
%_kde_bindir/kolf
%_kde_datadir/applications/kde4/kolf.desktop
%_kde_appsdir/kolf
%_kde_docdir/*/*/kolf
%_kde_datadir/icons/hicolor/*/apps/kolf.png

#-----------------------------------------------------------------------------

%package -n     konquest
Summary:        Conquer the planets of your enemy
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=konquest
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       konquest4
Obsoletes:      kde4-konquest < 1:4.0.68
Provides:       kde4-konquest = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n konquest
konquest: conquer the planets of your enemy

%files -n konquest
%defattr(-,root,root)
%_kde_bindir/konquest
%_kde_datadir/applications/kde4/konquest.desktop
%_kde_appsdir/konquest
%_kde_docdir/*/*/konquest
%_kde_datadir/icons/hicolor/*/apps/konquest.png


#-----------------------------------------------------------------------------

%package -n     ksame
Summary:        Collect pieces of the same color
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=ksame
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       ksame4
Obsoletes:      kde4-ksame < 1:4.0.68
Provides:       kde4-ksame = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n ksame
ksame: collect pieces of the same color

%files -n ksame
%defattr(-,root,root)
%_kde_bindir/ksame
%_kde_appsdir/ksame
%_kde_datadir/applications/kde4/ksame.desktop
%_kde_docdir/*/*/ksame
%_kde_datadir/icons/hicolor/*/apps/ksame.png

#-----------------------------------------------------------------------------

%package -n	kmahjongglib
Summary:	Common files for kmahjongg
Group:		Graphical desktop/KDE
Requires:	kdegames4-core
Conflicts:	kmahjongg < 1:4.3.1-4

%description -n kmahjongglib
Common files for kmahjongg.

%files -n kmahjongglib
%defattr(-,root,root)
%_kde_appsdir/kmahjongglib

#-----------------------------------------------------------------------------

%package -n     kmahjongg
Summary:        A tile laying patience
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kmahjongg
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91i
Conflicts:      kdegames4-core < 3.96.1-0.740193.1
Provides:       kmahjongg4
Obsoletes:      kde4-kmahjongg < 1:4.0.68
Provides:       kde4-kmahjongg = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kmahjongg
Kmahjongg: a tile laying patience

%files -n kmahjongg
%defattr(-,root,root)
%_kde_bindir/kmahjongg
%_kde_datadir/applications/kde4/kmahjongg.desktop
%_kde_appsdir/kmahjongg
%_kde_docdir/*/*/kmahjongg
%_kde_datadir/icons/hicolor/*/apps/kmahjongg.*
%_kde_datadir/config.kcfg/kmahjongg.kcfg

#-----------------------------------------------------------------------------

%package -n     kbattleship
Summary:        Battleship game with built-in game server
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kbattleship
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kbattleship4
Obsoletes:      kde4-kbattleship < 1:4.0.68
Provides:       kde4-kbattleship = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kbattleship
kbattleship: battleship game with built-in game server

%files -n kbattleship
%defattr(-,root,root)
%_kde_bindir/kbattleship
%_kde_datadir/applications/kde4/kbattleship.desktop
%_kde_docdir/*/*/kbattleship
%_kde_iconsdir/hicolor/*/apps/kbattleship.png
%_kde_appsdir/kbattleship
%_kde_datadir/kde4/services/kbattleship.protocol

#-----------------------------------------------------------------------------

%package -n     kiriki
Summary:        Kiriki: Close of Yahtzee 
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kiriki
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kiriki4
Obsoletes:      kde4-kiriki < 1:4.0.68
Provides:       kde4-kiriki = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kiriki
Kiriki is a dice game, written for KDE 4. 
It is a clone of Gnome Tali (gtali) that is a clone of Yahtzee!

%files -n kiriki
%defattr(-,root,root)
%_kde_bindir/kiriki
%_kde_datadir/applications/kde4/kiriki.desktop
%_kde_docdir/*/*/kiriki
%_kde_iconsdir/hicolor/*/apps/kiriki.png
%_kde_appsdir/kiriki

#-----------------------------------------------------------------------------

%package -n     ksudoku
Summary:        KSudoku - Play, create and solve sudoku grids 
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=ksudoku
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       ksudoku4
Obsoletes:      kde4-ksudoku < 1:4.0.68
Provides:       kde4-ksudoku = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n ksudoku
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

%files -n ksudoku
%defattr(-,root,root)
%_kde_bindir/ksudoku
%_kde_datadir/applications/kde4/ksudoku.desktop
%_kde_appsdir/ksudoku
%_kde_datadir/config/ksudokurc
%_kde_iconsdir/hicolor/*/apps/ksudoku.png
%_kde_docdir/*/*/ksudoku

#-----------------------------------------------------------------------------

%package -n     bovo
Summary:        Bovo: classic pen and paper game
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=bovo
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       bovo4
Obsoletes:      kde4-bovo < 1:4.0.68
Provides:       kde4-bovo = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n bovo
Bovo is a KDE 4 game, modeled upon a classic pen and paper game, 
where you try to connect five in a row prior to your opponent.

%files -n bovo
%defattr(-,root,root)
%_kde_bindir/bovo
%_kde_datadir/applications/kde4/bovo.desktop
%_kde_appsdir/bovo
%_kde_docdir/*/*/bovo

#-----------------------------------------------------------------------------

%package -n     kjumpingcube
Summary:        kjumpingcube: a tactical game for number-crunchers
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kjumpingcube
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Conflicts:      kdegames4-core < 3.96.1-0.740193.1
Provides:       kjumpingcube4
Obsoletes:      kde4-kjumpingcube < 1:4.0.68
Provides:       kde4-kjumpingcube = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kjumpingcube
KJumpingCube is a tactical one or two-player game. The playing field 
consists of squares that contains points which can be increased. By 
this you can gain more fields and finally win the board over.

%files -n kjumpingcube
%defattr(-,root,root)
%_kde_bindir/kjumpingcube
%_kde_datadir/applications/kde4/kjumpingcube.desktop
%_kde_appsdir/kjumpingcube
%_kde_datadir/config.kcfg/kjumpingcube.kcfg
%_kde_docdir/*/*/kjumpingcube
%_kde_iconsdir/hicolor/*/apps/kjumpingcube.png

#-----------------------------------------------------------------------------

%package -n     klines
Summary:        Place 5 equal pieces together, but wait, there are 3 new ones
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=klines
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Conflicts:      kdegames4-core < 3.96.1-0.740193.1
Provides:       klines4
Obsoletes:      kde4-klines < 1:4.0.68
Provides:       kde4-klines = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n klines
klines: place 5 equal pieces together, but wait, there are 3 new ones

%files -n klines
%defattr(-,root,root)
%_kde_bindir/klines
%_kde_datadir/applications/kde4/klines.desktop
%_kde_appsdir/klines
%_kde_docdir/*/*/klines
%_kde_iconsdir/hicolor/*/apps/klines.png
%_kde_datadir/config.kcfg/klines.kcfg

#-----------------------------------------------------------------------------

%package -n     kmines
Summary:        The classical mine sweeper
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kmines
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Conflicts:      kdegames4-core < 3.96.1-0.740193.1
Provides:       kmines4
Obsoletes:      kde4-kmines < 1:4.0.68
Provides:       kde4-kmines = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kmines
kmines: the classical mine sweeper

%files -n kmines
%defattr(-,root,root)
%_kde_bindir/kmines
%_kde_datadir/applications/kde4/kmines.desktop
%_kde_appsdir/kmines
%_kde_datadir/config/kmines.knsrc
%_kde_docdir/*/*/kmines
%_kde_iconsdir/hicolor/*/apps/kmines.png

#-----------------------------------------------------------------------------

%package -n     knetwalk
Summary:        Turn the board pieces to get all computers connected 
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=knetwalk
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       knetwalk4
Obsoletes:      kde4-knetwalk < 1:4.0.68
Provides:       kde4-knetwalk = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n knetwalk
Turn the board pieces to get all computers connected.

%files -n knetwalk
%defattr(-,root,root)
%_kde_bindir/knetwalk
%_kde_datadir/applications/kde4/knetwalk.desktop
%_kde_appsdir/knetwalk
%_kde_docdir/*/*/knetwalk
%_kde_iconsdir/hicolor/*/apps/knetwalk.*

#-----------------------------------------------------------------------------

%package -n     kpat
Summary:        Several patience card games
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kpat4
Obsoletes:      kde4-kpat < 1:4.0.68
Provides:       kde4-kpat = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kpat
kpat: several patience card games

%files -n kpat
%defattr(-,root,root)
%_kde_bindir/kpat
%_kde_datadir/applications/kde4/kpat.desktop
%_kde_appsdir/kconf_update/kpat_update_cardwidth.upd
%_kde_appsdir/kpat
%_kde_docdir/*/*/kpat
%_kde_iconsdir/hicolor/*/apps/kpat.png

#-----------------------------------------------------------------------------

%package -n     kshisen
Summary:        Patience game where you take away all pieces
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kshisen
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Conflicts:      kdegames4-core < 3.96.1-0.740193.1
Provides:       kshisen4
Obsoletes:      kde4-kshisen < 1:4.0.68
Provides:       kde4-kshisen = %epoch:%version

%description -n kshisen
Kshisen: patience game where you take away all pieces

%files -n kshisen
%defattr(-,root,root)
%_kde_bindir/kshisen
%_kde_datadir/applications/kde4/kshisen.desktop
%_kde_appsdir/kshisen
%_kde_datadir/sounds/kshisen
%_kde_datadir/config.kcfg/kshisen.kcfg
%_kde_iconsdir/hicolor/*/apps/kshisen*
%_kde_docdir/*/*/kshisen

#-----------------------------------------------------------------------------

%package -n     ktron
Summary:        Simple Tron clone
Group:          Graphical desktop/KDE
URL:        http://games.kde.org/game.php?game=ktron
Requires:       kdegames4-core
Provides:       ktron4
Conflicts:      kshisen < 1:4.2.95-2

%description -n ktron
Well known from the famous movie, KTron is a popular computer 
game for two players. In a fast action sequence both players 
have to move and avoid colliding with any walls, the opponent 
as well as the own path. The player colliding first looses the 
game.

%files -n ktron
%defattr(-,root,root)
%_kde_bindir/ktron
%_kde_datadir/applications/kde4/ktron.desktop
%_kde_appsdir/ktron
%_kde_datadir/config.kcfg/ktron.kcfg
%_kde_datadir/config/ktron.knsrc
%_kde_iconsdir/hicolor/*/*/ktron.png
%_kde_docdir/HTML/en/ktron

#-----------------------------------------------------------------------------

%package -n     kdesnake
Summary:        snake race played against the computer
Group:          Graphical desktop/KDE
URL:		    http://games.kde.org/game.php?game=kdesnake
Requires:       kdegames4-core
Provides:       kdesnake4 = %version
Provides:       ksnake = %version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kdesnake
KSnake Race is a fast action game where you steer a snake 
which has to eat food. While eating the snake grows. But 
once a player collides with the other snake or the wall 
the game is lost. This becomes of course more and more 
difficult the longer the snakes grow.

%files -n kdesnake
%defattr(-,root,root)
%_kde_bindir/kdesnake
%_kde_datadir/applications/kde4/kdesnake.desktop
%_kde_iconsdir/hicolor/*/*/kdesnake.*

#-----------------------------------------------------------------------------

%package -n     ksquares
Summary:        KSquares: an implementation of the popular paper based game squares
Group:          Graphical desktop/KDE
URL:        http://games.kde.org/game.php?game=ksquares
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Conflicts:      kdegames4-core < 3.96.1-0.740193.1
Provides:       ksquares4
Obsoletes:      kde4-ksquares < 1:4.0.68
Provides:       kde4-ksquares = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n ksquares
KSquares is an implementation of the popular paper based game squares. 
You must draw lines to complete squares, the player with the most s
quares wins.

%files -n ksquares
%defattr(-,root,root)
%_kde_bindir/ksquares
%_kde_datadir/applications/kde4/ksquares.desktop
%_kde_appsdir/ksquares
%_kde_datadir/config.kcfg/ksquares.kcfg
%_kde_iconsdir/hicolor/*/apps/ksquares.png
%_kde_docdir/*/*/ksquares

#-----------------------------------------------------------------------------

%package -n     kfourinline
Summary:        Place 4 pieces in a row
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kfourinline
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Conflicts:      kdegames4-core < 3.96.1-0.740193.1
Provides:       kfourinline4
Obsoletes:      kde4-kwin4 < 3.97.1-0.752247.1
Obsoletes:      kde4-kfourinline < 1:4.0.68
Provides:       kde4-kfourinline = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n kfourinline
kfourinline: place 4 pieces in a row

%files -n kfourinline
%defattr(-,root,root)
%_kde_bindir/kfourinline
%_kde_bindir/kfourinlineproc
%_kde_datadir/applications/kde4/kfourinline.desktop
%_kde_appsdir/kfourinline
%_kde_docdir/*/*/kfourinline
%_kde_iconsdir/hicolor/*/apps/kfourinline.png
%_kde_datadir/config.kcfg/kwin4.kcfg

#-----------------------------------------------------------------------------

%package -n     lskat
Summary:        Lieutnant skat
Group:          Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=lskat
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       lskat4
Obsoletes:      kde4-lskat < 1:4.0.68
Provides:       kde4-lskat = %epoch:%version
Conflicts:      kshisen < 1:4.2.95-2

%description -n lskat
lskat: lieutnant skat

%files -n lskat
%defattr(-,root,root)
%_kde_bindir/lskat
%_kde_datadir/applications/kde4/lskat.desktop
%_kde_appsdir/lskat
%_kde_docdir/*/*/lskat
%_kde_iconsdir/hicolor/*/apps/lskat.png

#-----------------------------------------------------------------------------

%package -n     kdiamond
Summary:        Three-in-a-row game
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kdiamond4
Conflicts:      kshisen < 1:4.2.95-2

%description -n kdiamond
KDiamond is a three-in-a-row game (much like Bejeweled) for the KDE 4 desktop.

%files -n kdiamond
%defattr(-,root,root)
%_kde_bindir/kdiamond
%_kde_datadir/applications/kde4/kdiamond.desktop
%_kde_appsdir/kdiamond
%_kde_datadir/config/kdiamond.knsrc
%_kde_iconsdir/*/*/*/kdiamond.*
%_kde_docdir/*/*/kdiamond
%_kde_datadir/sounds/KDiamond*

#-----------------------------------------------------------------------------

%package -n     kollision
Summary:        A simple ball dodging game
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kollision4
Conflicts:      kshisen < 1:4.2.95-2

%description -n kollision
A simple ball dodging game

%files -n kollision
%defattr(-,root,root)
%_kde_bindir/kollision
%_kde_datadir/applications/kde4/kollision.desktop
%_kde_appsdir/kollision
%_kde_iconsdir/*/*/apps/kollision.*
%_kde_docdir/*/*/kollision


#-----------------------------------------------------------------------------

%package -n     kubrick
Summary:        Game based on Rubik's Cube
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kubrick4
Conflicts:      kshisen < 1:4.2.95-2

%description -n kubrick
Kubrick, a game based on Rubik's Cube

%files -n kubrick
%defattr(-,root,root)
%_kde_bindir/kubrick
%_kde_datadir/applications/kde4/kubrick.desktop
%_kde_appsdir/kubrick
%_kde_docdir/*/*/kubrick
%_kde_iconsdir/hicolor/*/apps/kubrick.png

#-----------------------------------------------------------------------------

%package -n     kblocks
Summary:        Single player falling blocks puzzle game
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kblocks4
Conflicts:      kshisen < 1:4.2.95-2

%description -n kblocks
Single player falling blocks puzzle game

%files -n kblocks
%defattr(-,root,root)
%_kde_bindir/kblocks
%_kde_datadir/applications/kde4/kblocks.desktop
%_kde_appsdir/kblocks
%_kde_datadir/config.kcfg/kblocks.kcfg
%_kde_datadir/config/kblocks.knsrc
%_kde_docdir/HTML/en/kblocks
%_kde_iconsdir/hicolor/*/apps/kblocks.*

#-----------------------------------------------------------------------------

%package -n     kbreakout
Summary:        kbreakout
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       kbreakout4
Conflicts:      kshisen < 1:4.2.95-2

%description -n kbreakout
Single player falling blocks puzzle game

%files -n kbreakout
%defattr(-,root,root)
%{_kde_bindir}/kbreakout
%{_kde_datadir}/applications/kde4/kbreakout.desktop
%{_kde_appsdir}/kbreakout
%{_kde_iconsdir}/hicolor/*/apps/kbreakout.png
%_kde_docdir/*/*/kbreakout

#-----------------------------------------------------------------------------

%package -n     bomber
Summary:        Arcade bombing game
Group:          Graphical desktop/KDE
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       bomber4
Conflicts:      kshisen < 1:4.2.95-2

%description -n bomber
Arcade bombing game

%files -n bomber
%defattr(-,root,root)
%{_kde_bindir}/bomber
%{_kde_datadir}/applications/kde4/bomber.desktop
%{_kde_appsdir}/bomber
%{_kde_datadir}/config.kcfg/bomber.kcfg
%{_kde_docdir}/HTML/en/bomber
%{_kde_iconsdir}/hicolor/*/apps/bomber.*

#-----------------------------------------------------------------------------

%package -n     ksirk
Summary:        Computerized version of a well known strategy board game
Group:          Graphical desktop/KDE
URL:		    http://games.kde.org/game.php?game=ksirk
Requires:       kdegames4-core
Conflicts:      kdegames4 < 3.91
Provides:       ksirk4
Conflicts:      kshisen < 1:4.2.95-2

%description -n ksirk
KsirK is a computerized version of a well known strategy board game.
KsirK is a multi-player network-playable game with an AI. The goal
of the game is simply to conquer the World... It is done by attacking
your neighbours with your armies.

%files -n ksirk
%defattr(-,root,root)
%{_kde_bindir}/ksirk*
%{_kde_datadir}/applications/kde4/ksirk*.desktop
%{_kde_datadir}/config.kcfg/ksirk*settings.kcfg
%{_kde_datadir}/config/ksirk.knsrc
%{_kde_appsdir}/ksirk*
%{_kde_iconsdir}/*/*/apps/ksirk.png
%_kde_docdir/*/*/ksirk
%_kde_docdir/*/*/ksirkskineditor

#-----------------------------------------------------------------------------

%define libkdegames %mklibname kdegames 5
%define wronglibkdegames %mklibname kdegames 4

%package -n %libkdegames
Summary:    KDE 4 library
Group:      System/Libraries
Obsoletes:  %wronglibkdegames

%description -n %libkdegames
KDE 4 library.

%files -n %libkdegames
%defattr(-,root,root)
%_kde_libdir/libkdegames.so.*

#-----------------------------------------------------------------------------

%define libkmahjongglib %mklibname kmahjongglib 4

%package -n %libkmahjongglib
Summary: KDE 4 library
Group: System/Libraries
Requires: kmahjongglib = %{epoch}:%{version}
Conflicts:  %{_lib}kdegames4 < 3.91
Obsoletes:  %{_lib}kmahjongglib5 < 1:3.93.0-0.714146.1

%description -n %libkmahjongglib
KDE 4 library.

%files -n %libkmahjongglib
%defattr(-,root,root)
%_kde_libdir/libkmahjongglib.so.*

#-----------------------------------------------------------------------------

%define libkolfprivate %mklibname kolfprivate 4

%package -n %libkolfprivate
Summary: KDE 4 library
Group: System/Libraries
Conflicts:  %{_lib}kdegames4 < 3.91
Obsoletes: %{_lib}kolflib1.2.0 < 1:3.93.0-0.714146.1
Obsoletes: %{_lib}kolflib1 < 1:3.97.1-0.746784.1

%description -n %libkolfprivate
KDE 4 library.

%files -n %libkolfprivate
%defattr(-,root,root)
%_kde_libdir/libkolfprivate.so.*

#-----------------------------------------------------------------------------

%define libkggzgames %mklibname kggzgames 4

%package -n %libkggzgames
Summary: KDE 4 library
Group: System/Libraries
Conflicts:  %{_lib}kdegames4 < 3.91

%description -n %libkggzgames
KDE 4 library.

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

%files -n %libkggznet
%defattr(-,root,root)
%_kde_libdir/libkggznet.so.*

#-----------------------------------------------------------------------------

%define libiris_ksirk %mklibname iris_ksirk 2

%package -n %libiris_ksirk
Summary: KDE 4 library
Group: System/Libraries
Conflicts:  %{_lib}kdegames4 < 3.91

%description -n %libiris_ksirk
KDE 4 library.

%files -n %libiris_ksirk
%defattr(-,root,root)
%_kde_libdir/libiris_ksirk.so.*
#--------------------------------------------------------------------

%package devel
Summary:    Headers files for kdegames
Group:      Development/KDE and Qt
Obsoletes:  %{_lib}kdegames1-devel < 1:3.5.10-2
Requires:   kdelibs4-devel
Requires:   %libkdegames = %epoch:%version
Requires:   %libkmahjongglib = %epoch:%version
Requires:   %libkolfprivate = %epoch:%version
Requires:   %libkggzgames = %epoch:%version
Requires:   %libkggzmod = %epoch:%version
Requires:   %libkggznet = %epoch:%version
Requires:   %libiris_ksirk = %epoch:%version

%description devel
Headers files needed to build applications based on kdegames applications.

%files devel
%defattr(-,root,root,-)
%_kde_datadir/apps/cmake/modules/FindLibKDEGames.cmake
%_kde_datadir/apps/cmake/modules/GGZ.cmake
%_kde_libdir/*.so
%_kde_includedir/*

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdegames-%version%kde_snapshot

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

%clean
rm -fr %buildroot

