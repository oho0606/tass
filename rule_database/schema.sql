-- TASS Rule Database Schema (TASS-013)
-- SQLite SSOT

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS categories (
  category_code TEXT PRIMARY KEY,
  category_name TEXT NOT NULL,
  description TEXT,
  display_order INTEGER NOT NULL DEFAULT 0,
  enabled INTEGER NOT NULL DEFAULT 1,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS subcategories (
  subcategory_code TEXT PRIMARY KEY,
  category_code TEXT NOT NULL REFERENCES categories(category_code),
  subcategory_name TEXT NOT NULL,
  description TEXT,
  display_order INTEGER NOT NULL DEFAULT 0,
  enabled INTEGER NOT NULL DEFAULT 1,
  FOREIGN KEY (category_code) REFERENCES categories(category_code)
);

CREATE TABLE IF NOT EXISTS rules (
  rule_id TEXT PRIMARY KEY,
  rule_name TEXT NOT NULL,
  category_code TEXT NOT NULL REFERENCES categories(category_code),
  subcategory_code TEXT NOT NULL REFERENCES subcategories(subcategory_code),
  current_version TEXT NOT NULL DEFAULT '1.0.0',
  status TEXT NOT NULL,
  priority TEXT NOT NULL,
  weight REAL NOT NULL,
  description TEXT,
  author TEXT NOT NULL DEFAULT 'TASS Project',
  rule_type TEXT NOT NULL,
  spec_path TEXT,
  implementation_path TEXT,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_rules_category ON rules(category_code);
CREATE INDEX IF NOT EXISTS idx_rules_subcategory ON rules(subcategory_code);
CREATE INDEX IF NOT EXISTS idx_rules_status ON rules(status);
CREATE INDEX IF NOT EXISTS idx_rules_priority ON rules(priority);

CREATE TABLE IF NOT EXISTS rule_versions (
  rule_version_id TEXT PRIMARY KEY,
  rule_id TEXT NOT NULL REFERENCES rules(rule_id),
  version TEXT NOT NULL,
  change_log TEXT,
  status TEXT NOT NULL,
  approved_by TEXT,
  created_at TEXT NOT NULL,
  UNIQUE(rule_id, version)
);

CREATE INDEX IF NOT EXISTS idx_rule_versions_rule ON rule_versions(rule_id);

CREATE TABLE IF NOT EXISTS rule_parameters (
  parameter_id TEXT PRIMARY KEY,
  rule_id TEXT NOT NULL REFERENCES rules(rule_id),
  parameter_name TEXT NOT NULL,
  parameter_type TEXT NOT NULL,
  default_value TEXT,
  minimum TEXT,
  maximum TEXT,
  required INTEGER NOT NULL DEFAULT 1,
  description TEXT
);

CREATE TABLE IF NOT EXISTS rule_inputs (
  input_id TEXT PRIMARY KEY,
  rule_id TEXT NOT NULL REFERENCES rules(rule_id),
  input_name TEXT NOT NULL,
  input_type TEXT NOT NULL,
  required INTEGER NOT NULL DEFAULT 1,
  description TEXT
);

CREATE TABLE IF NOT EXISTS rule_outputs (
  output_id TEXT PRIMARY KEY,
  rule_id TEXT NOT NULL REFERENCES rules(rule_id),
  output_name TEXT NOT NULL,
  output_type TEXT NOT NULL,
  description TEXT
);

CREATE TABLE IF NOT EXISTS rule_dependencies (
  dependency_id TEXT PRIMARY KEY,
  rule_id TEXT NOT NULL REFERENCES rules(rule_id),
  depends_on_rule TEXT NOT NULL REFERENCES rules(rule_id),
  dependency_type TEXT NOT NULL CHECK (dependency_type IN ('Required', 'Optional'))
);

CREATE INDEX IF NOT EXISTS idx_rule_deps_rule ON rule_dependencies(rule_id);
CREATE INDEX IF NOT EXISTS idx_rule_deps_depends ON rule_dependencies(depends_on_rule);

CREATE TABLE IF NOT EXISTS rule_tags (
  tag_id TEXT PRIMARY KEY,
  rule_id TEXT NOT NULL REFERENCES rules(rule_id),
  tag TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_rule_tags_rule ON rule_tags(rule_id);
CREATE INDEX IF NOT EXISTS idx_rule_tags_tag ON rule_tags(tag);

CREATE TABLE IF NOT EXISTS rule_tests (
  test_id TEXT PRIMARY KEY,
  rule_id TEXT NOT NULL REFERENCES rules(rule_id),
  test_name TEXT NOT NULL,
  test_type TEXT NOT NULL CHECK (test_type IN ('Unit', 'Integration', 'Regression')),
  status TEXT NOT NULL,
  coverage REAL,
  last_run TEXT
);

CREATE TABLE IF NOT EXISTS rule_backtests (
  backtest_id TEXT PRIMARY KEY,
  rule_id TEXT NOT NULL REFERENCES rules(rule_id),
  market TEXT NOT NULL,
  timeframe TEXT NOT NULL,
  start_date TEXT,
  end_date TEXT,
  dataset TEXT,
  version TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS rule_performance (
  performance_id TEXT PRIMARY KEY,
  backtest_id TEXT NOT NULL REFERENCES rule_backtests(backtest_id),
  win_rate REAL,
  profit_factor REAL,
  sharpe_ratio REAL,
  sortino_ratio REAL,
  calmar_ratio REAL,
  cagr REAL,
  maximum_drawdown REAL,
  average_profit REAL,
  average_loss REAL,
  trade_count INTEGER
);

CREATE TABLE IF NOT EXISTS rule_lifecycle (
  lifecycle_id TEXT PRIMARY KEY,
  rule_id TEXT NOT NULL REFERENCES rules(rule_id),
  stage TEXT NOT NULL,
  started_at TEXT NOT NULL,
  completed_at TEXT
);

CREATE INDEX IF NOT EXISTS idx_rule_lifecycle_rule ON rule_lifecycle(rule_id);

CREATE TABLE IF NOT EXISTS rule_history (
  history_id TEXT PRIMARY KEY,
  rule_id TEXT NOT NULL REFERENCES rules(rule_id),
  version TEXT NOT NULL,
  field TEXT NOT NULL,
  old_value TEXT,
  new_value TEXT,
  changed_by TEXT NOT NULL,
  changed_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_rule_history_rule ON rule_history(rule_id);

CREATE TABLE IF NOT EXISTS rule_aliases (
  alias_id TEXT PRIMARY KEY,
  rule_id TEXT NOT NULL REFERENCES rules(rule_id),
  alias TEXT NOT NULL UNIQUE
);

CREATE INDEX IF NOT EXISTS idx_rule_aliases_alias ON rule_aliases(alias);
