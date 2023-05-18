from datetime import datetime, timedelta
import math
import pandas
from typing import Optional
from fastapi import Depends, HTTPException
from dto.dto_common import TokenData
from dto.dto_transaction import InputTransaction, OutputTransactionPage
from enums.enum_tipe import Tipe
from model.model_transaction import Transaction
from repository.repository_transaction import RepositoryTransaction


class ServiceTransaction:
    def __init__(
        self, repository_transaction: RepositoryTransaction = Depends()
    ) -> None:
        self.repository_transaction = repository_transaction

    def insert_new_transaction(
        self, input_transaction: InputTransaction, current_user: TokenData
    ):
        new_transaction = Transaction(
            tipe=input_transaction.tipe,
            amount=input_transaction.amount,
            notes=input_transaction.notes,
            method=input_transaction.method,
            user_id=current_user.userId,
        )
        return self.repository_transaction.insert_new_transaction(new_transaction)

    def get_list_transaction(
        self, tipe: Tipe, page: int, size: int, current_user: TokenData
    ):
        match_filter = {"user_id": current_user.userId}
        if tipe is not None:
            match_filter["tipe"] = tipe

        skip = page * size
        total_data = self.repository_transaction.count_list_transaction(match_filter)
        list_transaction = self.repository_transaction.get_list_transaction(
            match_filter, skip, size
        )
        total_page = math.ceil(total_data / size)

        return OutputTransactionPage(
            page=page,
            size=size,
            total_data=total_data,
            total_page=total_page,
            data=list_transaction,
        )

    def export_transaction(
        self,
        tipe: Tipe,
        start_date: datetime,
        end_date: datetime,
        current_user: TokenData,
    ):
        match_filter = {"user_id": current_user.userId}
        if tipe is not None:
            match_filter["tipe"] = tipe

        if start_date is not None and end_date is not None:
            match_filter["created_time"] = {
                "$gte": start_date,
                "$lt": end_date + timedelta(days=1),
            }

        projection_stage = Transaction.project_export()

        result = self.repository_transaction.export_list_transaction(
            match_filter, projection_stage
        )

        if len(result) == 0:
            raise HTTPException(status_code=400, detail="No data to be exported")

        df = pandas.DataFrame(result)

        file_name = "History_Transaksi.csv"
        content_file = df.to_csv(sep=";")
        return content_file, file_name
