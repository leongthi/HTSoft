//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace CR_API.Models
{
    using System;
    
    public partial class ws_Ticket_Estimations_Detail_Get_Result
    {
        public int TicketID { get; set; }
        public string DesignScreen { get; set; }
        public Nullable<decimal> TotalDesignScreen { get; set; }
        public string LogicScreen { get; set; }
        public Nullable<decimal> TotalLogicScreen { get; set; }
        public string SPScreen { get; set; }
        public Nullable<decimal> TotalSPScreen { get; set; }
        public string DesignReport { get; set; }
        public Nullable<decimal> TotalDesignReport { get; set; }
        public string SPReport { get; set; }
        public Nullable<decimal> TotalSPReport { get; set; }
        public Nullable<decimal> DevUnitTest { get; set; }
        public Nullable<decimal> DevFixBug { get; set; }
        public string Other { get; set; }
        public Nullable<decimal> TotalOther { get; set; }
        public Nullable<int> CreatedBy { get; set; }
        public Nullable<System.DateTime> CreatedOn { get; set; }
        public Nullable<System.DateTime> ModifiedOn { get; set; }
        public Nullable<int> ModifiedBy { get; set; }
    }
}
