"use client";

import { FormEvent, useState } from "react";

type Message = { role: "user" | "assistant"; content: string };
const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export default function Home() {
  const [conversationId, setConversationId] = useState<number | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function sendMessage(event: FormEvent) {
    event.preventDefault();
    const message = input.trim();
    if (!message || loading) return;
    setInput("");
    setError("");
    setMessages((current) => [...current, { role: "user", content: message }]);
    setLoading(true);
    try {
      const response = await fetch(`${API_URL}/api/v1/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ conversation_id: conversationId, user_id: 1, message }),
      });
      if (!response.ok) throw new Error("ATLAS could not answer right now.");
      const data = await response.json();
      setConversationId(data.conversation_id);
      setMessages((current) => [...current, { role: "assistant", content: data.message }]);
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="shell">
      <header className="topbar">
        <div className="brand-mark">A</div>
        <div>
          <p className="eyebrow">Personal AI operating system</p>
          <h1>ATLAS</h1>
        </div>
        <span className="status"><i /> Local foundation</span>
      </header>
      <section className="chat-panel" aria-label="ATLAS chat">
        <div className="messages" aria-live="polite">
          {messages.length === 0 ? (
            <div className="empty-state">
              <span className="compass">✦</span>
              <h2>What are we working on?</h2>
              <p>Start a conversation. Your messages will be persisted locally.</p>
            </div>
          ) : messages.map((message, index) => (
            <div className={`message-row ${message.role}`} key={`${message.role}-${index}`}>
              <div className="message-bubble">{message.content}</div>
            </div>
          ))}
          {loading && <div className="message-row assistant"><div className="message-bubble typing">Thinking<span>.</span><span>.</span><span>.</span></div></div>}
        </div>
        {error && <p className="error" role="alert">{error}</p>}
        <form className="composer" onSubmit={sendMessage}>
          <input value={input} onChange={(event) => setInput(event.target.value)} placeholder="Message ATLAS" aria-label="Message ATLAS" maxLength={10000} />
          <button type="submit" disabled={loading || !input.trim()} aria-label="Send message">Send</button>
        </form>
      </section>
      <footer>V1 foundation <span>•</span> Conversations are stored in PostgreSQL</footer>
    </main>
  );
}


