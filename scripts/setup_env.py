#!/usr/bin/env python3
"""
Environment setup script for FastAPI AWS Services
Usage: python scripts/setup_env.py [development|staging|production]
"""

import os
import sys
import shutil
from pathlib import Path

def setup_environment(env_name: str):
    """Setup environment by copying the appropriate config file"""
    project_root = Path(__file__).parent.parent
    config_file = project_root / f"config.env.{env_name}"
    target_file = project_root / ".env"
    
    if not config_file.exists():
        print(f"Configuration file {config_file} not found!")
        print("Available environments:")
        for env_file in project_root.glob("config.env.*"):
            print(f"  - {env_file.name.replace('config.env.', '')}")
        sys.exit(1)
    
    # Copy the environment-specific config to .env
    shutil.copy2(config_file, target_file)
    print(f"Environment set to: {env_name}")
    print(f"Configuration copied from: {config_file}")
    print(f"Target file: {target_file}")
    
    # Show important reminders
    if env_name == "production":
        print("\nPRODUCTION ENVIRONMENT SETUP:")
        print("   - Make sure to change the SECRET_KEY!")
        print("   - Verify all AWS credentials are correct")
        print("   - Check database connection settings")
        print("   - Review CORS and security settings")
    elif env_name == "staging":
        print("STAGING ENVIRONMENT SETUP:")
        print("   - Verify staging database credentials")
        print("   - Check AWS staging bucket configuration")
        print("   - Review CORS origins for staging domains")

def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/setup_env.py [development|staging|production]")
        print("\nExamples:")
        print("  python scripts/setup_env.py development")
        print("  python scripts/setup_env.py staging")
        print("  python scripts/setup_env.py production")
        sys.exit(1)
    
    env_name = sys.argv[1].lower()
    valid_environments = ["development", "staging", "production"]
    
    if env_name not in valid_environments:
        print(f"Invalid environment: {env_name}")
        print(f"Valid environments: {', '.join(valid_environments)}")
        sys.exit(1)
    
    setup_environment(env_name)

if __name__ == "__main__":
    main()
