# GobCog Adventure

A feature-rich RPG adventure cog for Red-DiscordBot, enabling text-based dungeon crawling, loot collection, and character progression across Discord servers.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Red-DiscordBot](https://img.shields.io/badge/Red--DiscordBot-Cog-red)
![Discord](https://img.shields.io/badge/Discord-Bot-purple)

> Forked from [locastan's adventure cog](https://github.com/locastan/gobcog) with significant enhancements.

## Overview

An interactive Discord bot cog that transforms servers into collaborative RPG adventures. Players join forces to battle monsters, collect loot, level up characters, and compete for rare items. Supports multi-server play with persistent character data.

## Features

### Core Gameplay
- **Collaborative Adventures** - Multiple players join to attack, talk, pray, or flee
- **Character Classes** - Tinkerer, Berserker, Cleric, Ranger, Bard (unlocked at level 10)
- **Loot System** - Chests with rarity tiers (normal, .rare, [epic])
- **Negaverse** - PvP arena for bonus XP using earned credits

### Enhancements Over Original
- **Config-Based Storage** - Atomic user attribute saving via Red's Config
- **2,800+ Monster Combinations** - Expanded stat/monster combinations
- **300% More Gear** - Significantly expanded item pool
- **Double Item Slots** - More equipment customization
- **Multi-Server Support** - Play on multiple servers simultaneously

### Class Abilities

| Class | Ability | Description |
|-------|---------|-------------|
| **Tinkerer** | Forge | Combine two items into a soul-bound device |
| **Berserker** | Rage | Big attack bonus with fumble risk |
| **Cleric** | Bless | Heal and buff the entire party |
| **Ranger** | Pet | Companion that finds items and bonuses |
| **Bard** | Music | Aid diplomacy attempts |

## Tech Stack

| Component | Technology |
|-----------|------------|
| **Framework** | Red-DiscordBot 3.x |
| **Language** | Python 3.8+ |
| **Data Storage** | Red Config (JSON-backed) |
| **Discord API** | discord.py |

## Commands

### Player Commands

```
[p]adventure          # Start a group adventure
[p]stats              # View your character stats
[p]backpack           # View your equipment and inventory
[p]loot <rarity>      # Open a loot chest
[p]heroclass          # Choose/view your class (level 10+)
[p]negaverse <bet>    # Enter PvP arena
```

### Class-Specific Commands

```
[p]forge              # (Tinkerer) Combine items
[p]rage               # (Berserker) Enter rage mode
[p]bless              # (Cleric) Bless the party
[p]pet                # (Ranger) Pet management
[p]music              # (Bard) Perform for diplomacy
```

### Admin Commands

```
[p]adventureset cart <#channel>  # Configure merchant cart channel
```

## Adventure Mechanics

### Combat Options
- 🗡️ **Attack** - Fight the monster with strength
- 🗨️ **Talk** - Attempt diplomacy with charisma
- 🛐 **Pray** - Call upon Herbert (or custom deity) for aid
- 🏃‍♀️ **Run** - Flee from the encounter

### Loot Rarity

```css
normal items look like this
.rare_items_look_like_this
[epic items look like this]
```

## Installation

### Prerequisites
- Red-DiscordBot 3.x installed and configured
- Bot instance running

### Setup

```bash
# Add repository
[p]repo add gobcog https://github.com/Kevin-Mok/gobcog

# Install cog
[p]cog install gobcog adventure

# Load cog
[p]load adventure
```

## Why This Project is Interesting

### Technical Highlights

1. **Discord Bot Development**
   - Async Python with discord.py
   - Reaction-based interactive gameplay
   - Multi-user concurrent game sessions

2. **Data Architecture**
   - Config-based persistence for reliability
   - Atomic saves preventing data corruption
   - Cross-server character portability

3. **Game Design**
   - Balanced progression system
   - Class-based ability differentiation
   - Collaborative mechanics encouraging engagement

4. **Large-Scale Content**
   - 2,800+ procedural monster variations
   - Extensive gear database
   - Rarity-weighted loot tables

### Skills Demonstrated

- **Python Development**: Async/await patterns, OOP design
- **Discord API**: Reactions, embeds, commands framework
- **Game Systems**: RPG mechanics, stat balancing, progression curves
- **Data Management**: Persistent storage, migration, multi-tenant data

## Future Improvements

- End-of-game HP display (total hit vs mob points)
- Stackable backpack items
- Tradeable loot boxes
- Alternate stats (dexterity, agility, critical chance)
- Player races with scaling bonuses
- Revamped roll calculations for high-level balance

## Resume-ready points by variant

### `general`
- Enhanced a Red-DiscordBot RPG cog with persistent progression, richer loot systems, and multi-server support for sustained community engagement.
- Expanded gameplay depth through class abilities, negaverse PvP, and large procedural content sets while preserving operational reliability.

### `web-dev`
- Engineered interactive command-driven UX where users coordinate real-time decisions, mirroring complex web interaction design patterns.
- Built clear command surfaces and response feedback loops that reduce friction in multi-user asynchronous gameplay flows.

### `aws`
- Designed persistence and state-management patterns that support reliable scaling and operational resilience for always-on bot environments.
- Applied reliability-first architecture with atomic config saves and multi-tenant data handling aligned to cloud-operations expectations.

### `python`
- Developed async Python game systems using discord.py and Red Config, with modular mechanics for combat, loot, and class abilities.
- Implemented persistent RPG logic and concurrent session handling, demonstrating Python-first architecture for real-time user interactions.

### `aws-web-dev`
- Combined user-facing interaction design with operational safeguards, balancing feature richness and reliability in live community systems.
- Structured gameplay workflows to support scalable hosting, observability, and long-running service maintenance.

### `aws-python`
- Built automation-heavy Python bot workflows with persistent storage, concurrency handling, and operational guardrails suitable for cloud hosting.
- Emphasized maintainable async service design that supports scaling and incident response in production-like environments.

### `web-dev-django`
- Designed command and state-transition patterns transferable to Django-backed multiplayer systems with strict data integrity requirements.
- Built modular gameplay logic that aligns with Django model-driven domains and server-side orchestration patterns.

### `it-support`
- Created clear command documentation and predictable system behavior, improving triage speed for gameplay and configuration issues.
- Reduced operational ambiguity with structured user flows that help moderators and support staff resolve player problems quickly.

### `it-support-aws`
- Implemented observable, persistent service behavior that helps support teams isolate incidents across multi-server deployments.
- Built failure-aware state handling to improve support coordination between community operations and infrastructure maintainers.

### `sales`
- Increased product differentiation through deep feature expansion, helping position the bot as a premium community-engagement experience.
- Combined measurable content scale and stability improvements to strengthen value messaging for server operators.

### `call-centre`
- Designed clarity-first command interactions that reduce repetitive questions and improve response consistency in busy Discord communities.
- Structured support-friendly user pathways that help moderators handle high interaction volume with less escalation.

## Contributing

PRs welcome! Please open an issue first to discuss proposed changes. Feature requests should be submitted as GitHub issues, not via Discord DMs.

## Author

[Kevin Mok](https://github.com/Kevin-Mok)
