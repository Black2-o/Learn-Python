from mcp.server.fastmcp import FastMCP
import os   


mcp = FastMCP("AI Sticky Notes")

NOTES_FILES = os.path.join(os.path.dirname(__file__), "notes.txt")


def ensure_file():
    if not os.path.exists(NOTES_FILES):
        with open(NOTES_FILES, "w") as f:
            f.write("")



@mcp.tools()
def add_note(message: str) -> str:
    """
    Append a new Note to the sticky notes files.

    Args: 
        message(str): The note content to be added.
    Return:
        str: Confirmation message indecating the note was saved. 
    """
    ensure_file()
    with open(NOTES_FILES, "a") as f:
        f.write(message + "\n")
    return "Note added!"


@mcp.tools()
def get_notes() -> str:
    """
    Read and return all notes from the sticky note file.
    Return: 
        str: All notes as a single string.saparated by line breacks. 
        If no note exists, a default message return 
    """
    ensure_file()
    with open(NOTES_FILES, "r") as f:
        notes = f.read().strip()
    return notes or "No notes found."

@mcp.resource("notes://latest")
def _get_latest_note() -> str:
    """
    Get the most recently added note from the sticky note file.

    Returns:
        str: The last note entry. If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILES, "r") as f:
        notes = f.readlines()
    return notes[-1].strip() if lines else "No notes found."


@mcp.prompt()
def note_summary_prompt() -> str:
    """
    Generate a prompt asking the AI to summarize all current notes.

    Returns:
        str: A prompt string that includes all notes and asks for a summary.
             If no notes exist, a message will be shown indicating that.
    """
    ensure_file()
    with open(NOTES_FILES, "r") as f:
        notes = f.read.strip()
    if not notes:
        return "No Notes Found"
    return f"Summarize the current notes: {content}"
