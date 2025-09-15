# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Ren'Py visual novel project documenting D&D campaign sessions. The game allows readers to experience party adventures through an interactive story format, with each session adapted as scenes with branching choices.

## Development Commands

### Running the Game
- Use the Ren'Py launcher GUI (recommended): Open `tools/renpy-8.4.1-sdk/` launcher
- Command line: `tools/renpy-8.4.1-sdk/renpy .` (from project root)
- On macOS: `tools/renpy-8.4.1-sdk/renpy` (executable available)

### Building Distribution
- Use Ren'Py launcher's "Build Distributions" option
- Builds to `/build/` and `/dist/` directories (git-ignored)

## Project Architecture

### Core Game Structure
- `game/script.rpy` - Main story script with session content
- `game/options.rpy` - Game configuration and metadata
- `game/screens.rpy` - UI screen definitions
- `game/gui.rpy` - Interface styling and theming

### Session Organization
Each D&D session follows this pattern:
- Session entry label (e.g., `label session_66`)
- Sequential scene labels (e.g., `session66_scene1`, `session66_scene2`)
- Menu systems for branching exploration of parallel events
- Character definitions at top of script.rpy with color-coded dialogue

### Character System
Characters are defined with color-coded dialogue:
- Party members: `thrall`, `granite`, `harold`, `ronin`, `rime`
- NPCs: `mouth`, `rysen`, `ccillian`, `shallar`, etc.
- Groups: `children_of_reath`, `host_family`
- Special: `dm`, `narrator`

### Assets Organization
- `game/images/` - Character sprites, backgrounds, UI graphics
- `game/audio/` - Music and sound effects
- `game/gui/` - UI theme assets and styling graphics

### Development Planning
- `planning/` - Session outlines and story planning documents
- Scene breakdowns follow: Where/Who/Beat structure
- Planning documents guide script.rpy scene implementation

## Ren'Py Specific Notes

### File Types
- `.rpy` - Source scripts (edit these)
- `.rpyc` - Compiled bytecode (auto-generated, git-ignored)
- Assets load automatically from `game/images/` and `game/audio/`

### Scene Transitions
Standard transitions used: `fade`, `dissolve`, `with dissolve`
Configured in options.rpy for consistency

### Development Workflow
1. Plan session content in `planning/` directory
2. Add character definitions to script.rpy if needed
3. Implement scenes with labels and dialogue
4. Add background/image references (implement assets later)
5. Test via Ren'Py launcher
6. Build distributions when ready for release

## Important Notes

- Tools directory (`tools/renpy-8.4.1-sdk/`) contains full Ren'Py installation
- Game saves and cache are git-ignored but persist locally
- Build outputs excluded from version control
- Project configured as "Rime's Recollection" v1.0