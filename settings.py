class Settings:
  """A class to store all settings for Alien Invasion."""

  def __init__(self):
    """Initialize the game's static settings."""
    # Screen settings
    self.screen_width = 1200
    self.screen_height = 1200
    self.bg_color = (255, 255, 255) 

    # Ship settings
    self.ship_speed = 1.7
    self.ship_limit = 3

    # Bullet settings
    self.bullet_speed = 1.5
    self.bullet_width = 7
    self.bullet_height = 25
    self.bullet_color = (255, 64, 64)
    self.bullets_allowed = 4

    # Alien settings
    self.alien_speed = 0.8
    self.fleet_drop_speed = 16
    # fleet_direction of 1 represents right; -1 represents left.
    self.fleet_direction = 1

    # How quickly the game speeds up
    self.speedup_scale = 1.16

    self.initialize_dynamic_settings()

    self.new_rows = 0
  
  def initialize_dynamic_settings(self):
    """Initialize settings that change throughout the game."""
    self.ship_speed = 1.5
    self.bullet_speed = 3.0
    self.alien_speed = 1.0

    # fleet_direction of 1 represents right; -1 represents left.
    self.fleet_direction = 1

    # Scoring
    self.alien_points = 50

  def increase_speed(self):
    """Increase speed settings."""
    self.ship_speed *= self.speedup_scale
    self.bullet_speed *= self.speedup_scale
    self.alien_speed *= self.speedup_scale
    self.fleet_drop_speed *= self.speedup_scale
    self.bullet_speed *= self.speedup_scale

    

