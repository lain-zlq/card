class CardWarning(Warning):
    """Base warning for Card."""
class CardDependencyWarning(CardWarning):
    """An imported dependency doesn't match the expected version range."""