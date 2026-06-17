from database.models import Fatos

class Loader:
    async def insert(self, rows: list) -> None:
        """
        Insere um conjunto de fatos no banco.
        """
        events = []
        print(len(rows))
        
        for row in rows:
            event = Fatos(**row)
            events.append(event)

        if events:
            await Fatos.bulk_create(events, batch_size=1000, ignore_conflicts=True)
