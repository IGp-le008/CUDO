"""PostgreSQL initialization with pgvector support."""

-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create indices for performance
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_registration_number ON users(registration_number);
CREATE INDEX IF NOT EXISTS idx_chat_messages_session_id ON chat_messages(session_id);
CREATE INDEX IF NOT EXISTS idx_chat_messages_user_id ON chat_messages(user_id);
CREATE INDEX IF NOT EXISTS idx_seat_allocations_program_id ON seat_allocations(program_id);
CREATE INDEX IF NOT EXISTS idx_student_results_student_id ON student_results(student_id);
CREATE INDEX IF NOT EXISTS idx_notices_published_at ON notices(published_at);
CREATE INDEX IF NOT EXISTS idx_knowledge_base_category ON knowledge_base(category);

-- Create full-text search index for knowledge base
CREATE INDEX IF NOT EXISTS idx_knowledge_base_search ON knowledge_base USING GIN(to_tsvector('english', content));
