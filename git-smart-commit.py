import typer
from rich.console import Console
from git import Repo, InvalidGitRepositoryError
import openai
import os

app = typer.Typer()
console = Console()

# Set your OpenAI API key (can also use environment variable OPENAI_API_KEY)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Model to use
OPENAI_MODEL = "gpt-4o-mini"


def get_repo_and_root(path: str = ".") -> tuple[Repo, str]:
    try:
        repo = Repo(path, search_parent_directories=True)
        root = repo.git.rev_parse("--show-toplevel")
        return repo, root
    except InvalidGitRepositoryError:
        console.print("[red]Error: Not inside a git repository.[/red]")
        raise typer.Exit(1)


def get_staged_diff() -> str:
    repo, root = get_repo_and_root()
    repo = Repo(root)  # Ensure repo is rooted at the top-level
    diff = repo.git.diff('--cached')
    return diff


def generate_commit_message(diff: str) -> str:
    if not OPENAI_API_KEY:
        raise RuntimeError("OpenAI API key not set. Set OPENAI_API_KEY environment variable.")
    client = openai.Client(api_key=OPENAI_API_KEY)
    prompt = (
        "You are an expert software engineer. "
        "Write a concise, clear, and conventional git commit message for the following staged diff. "
        "Use present tense and follow best practices.\n\nDiff:\n" + diff
    )
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()


@app.command()
def main():
    """Generate a smart commit message using AI based on staged changes."""
    console.print("[bold cyan]Extracting staged diff...[/bold cyan]")
    diff = get_staged_diff()
    if not diff.strip():
        console.print("[yellow]No staged changes found. Please stage your changes first.[/yellow]")
        raise typer.Exit(1)
    console.print("[bold cyan]Generating commit message with GPT-4o-mini...[/bold cyan]")
    try:
        commit_message = generate_commit_message(diff)
        console.print("[green]Suggested commit message:[/green]\n")
        console.print(f"{commit_message}")
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()